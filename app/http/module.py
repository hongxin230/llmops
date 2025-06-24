#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : module.py
@Time    : 2025/6/16 17:18
@Author  : zhaohongxin621@126.com
"""
from flask_migrate import Migrate
from injector import Binder, Module

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
