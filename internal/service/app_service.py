#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : app_service.py
@Time    : 2025/6/17 16:08
@Author  : zhaohongxin621@126.com
"""
import uuid
from dataclasses import dataclass

from injector import inject

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.auto_commit:
            # 1.创建模型实体类
            app = App(name="测试机器人", icon="", description="这是一个简单的聊天机器人", account_id=uuid.uuid4())
            # 2.将实体类加载到session会话中
            self.db.session.add(app)
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit:
            app = self.get_app(id)
            app.name = "慕课聊天机器人"
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit:
            app = self.get_app(id)
            self.db.session.delete(app)
        return app
