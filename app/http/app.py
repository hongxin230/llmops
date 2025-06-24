#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : app.py
@Time    : 2025/6/12 11:54
@Author  : zhaohongxin621@126.com
"""
import dotenv
from flask_migrate import Migrate
from injector import Injector, singleton

from config import Config
from internal.extension import db  # 从统一位置导入
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy

# 加载环境变量
dotenv.load_dotenv()

injector = Injector()
injector.binder.bind(SQLAlchemy, to=db, scope=singleton)  # 关键！绑定全局 db

conf = Config()

app = Http(__name__,
           conf=conf,
           db=db,
           migrate=injector.get(Migrate),
           router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
