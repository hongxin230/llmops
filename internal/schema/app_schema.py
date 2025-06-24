#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : app_schema.py
@Time    : 2025/6/13 16:49
@Author  : zhaohongxin621@126.com
"""

from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求"""
    # 必填，长度2000
    query = StringField("query", validators=[
        DataRequired("用户提问必填"),
        Length(max=2000, message="提问最大长度2000")
    ])
