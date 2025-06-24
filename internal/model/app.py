#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : app.py
@Time    : 2025/6/17 15:01
@Author  : zhaohongxin621@126.com
"""
import uuid
from datetime import datetime

from sqlalchemy import (
    Index
)
from sqlalchemy.dialects.postgresql import UUID  # ✅ 使用PostgreSQL专用UUID类型

from internal.extension.database_extension import db

print(f"模型使用的db实例ID: {id(db)}")  # 添加调试输出


class App(db.Model):
    """AI应用基础模型类"""
    __tablename__ = "app"
    __table_args__ = (
        Index("idx_app_account_id", "account_id"),
    )

    id = db.Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)
    account_id = db.Column(UUID, nullable=False)  # 统一使用 db.Column
    name = db.Column(db.String(255), default="", nullable=False)  # 使用 db.String
    status = db.Column(db.String(255), default="", nullable=False)  # 使用 db.String
    icon = db.Column(db.String(255), default="", nullable=False)
    description = db.Column(db.Text, default="", nullable=False)  # 使用 db.Text
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
