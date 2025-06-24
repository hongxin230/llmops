#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 2.字符串提示拼接.py
@Time    : 2025/6/19 16:35
@Author  : zhaohongxin621@126.com
"""
from langchain_core.prompts import PromptTemplate

prompt = (
        PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
        + ",让我开心下"
        + "\n使用{language}语言"
)

print(prompt)

print(prompt.invoke({"subject": "程序员", "language": "zh"}).to_string())
