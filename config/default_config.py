#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : default_config.py
@Time    : 2025/6/16 16:56
@Author  : zhaohongxin621@126.com
"""

# 应用默认配置
DEFAULT_CONFIG = {
    "WTF_CSRF_ENABLED": False,
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_POOL_SIZE": 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True"
}
