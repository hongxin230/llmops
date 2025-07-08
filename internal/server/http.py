#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : http.py
@Time    : 2025/6/12 11:47
@Author  : zhaohongxin621@126.com
"""
import os
import traceback

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import inspect

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import Response, json, HttpCode
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    """http服务引擎"""

    def __init__(self,
                 *args,
                 conf: Config,
                 db: SQLAlchemy,
                 migrate: Migrate,
                 router: Router,
                 **kwargs):
        # 1.调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 2.初始化应用配置
        self.config.from_object(conf)

        self.config['SQLALCHEMY_ECHO'] = True  # 开启SQL日志

        # 3.配置CORS（关键位置！必须在其他初始化之前）
        self._configure_cors()

        # 3.注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 4.初始化flask扩展
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")
        # 验证数据库连接
        with self.app_context():
            try:
                # db.create_all()
                inspector = inspect(db.engine)
                print("创建的表:", inspector.get_table_names())
            except Exception as e:
                print("数据库初始化失败:", e)
                traceback.print_exc()  # ← 一定要把这行加上
                raise

        # 5.注册应用路由
        router.register_router(self)

    def _configure_cors(self):
        """配置跨域白名单"""
        CORS(self, resources={
            r"/*": {
                "origins": ["http://localhost:5173"],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True,
                "max_age": 86400
            }
        })

        # 确保所有响应都包含 CORS 头
        @self.after_request
        def add_cors_headers(response):
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            return response
        
    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))
        if self.debug or os.getenv('FLASK_ENV') == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
