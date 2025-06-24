# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : flask_sqlalchemy.py
@Time    : 2025/6/12 10:50
@Author  : zhaohongxin621@126.com
"""
from .database_extension import db
from .migrate_extension import migrate

__all__ = ["db", "migrate"]
