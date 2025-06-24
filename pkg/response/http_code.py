#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : http_code.py
@Time    : 2025/6/16 10:01
@Author  : zhaohongxin621@126.com
"""
from enum import Enum


class HttpCode(str, Enum):
    """Http基础状态码"""
    SUCCESS = "success"  # 成功状态
    FAIL = "fail"  # 失败状态
    NOT_FOUND = "not_found"  # 未找到状态
    UNAUTHORIZED = "unauthorized"  # 未授权状态
    FORBIDDEN = "forbidden"  # 禁止访问状态
    VALIDATE_ERROR = "validate_error"  # 验证错误状态
