#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : response.py
@Time    : 2025/6/16 10:05
@Author  : zhaohongxin621@126.com
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    return jsonify(data), 200


def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def validation_error_json(errors: dict = None):
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors[first_key]
    else:
        msg = first_key[0]
    return json(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=errors))


def message(code: HttpCode = None, msg: str = ""):
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """未授权"""
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """无权限"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)
