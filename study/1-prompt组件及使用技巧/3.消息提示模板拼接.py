#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 3.消息提示模板拼接.py
@Time    : 2025/6/19 16:44
@Author  : zhaohongxin621@126.com
"""
from langchain_core.prompts import ChatPromptTemplate

system_chat_template = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户提问进行回复，我是{username}")
])

human_chat_template = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])

chat_prompt = system_chat_template + human_chat_template

print(chat_prompt.invoke({"username": "慕课", "query": "你好，你是谁？"}))
