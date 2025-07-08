#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.对话消息历史组件基础.py
@Time    : 2025/7/7 11:51
@Author  : zhaohongxin621@126.com
"""

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()
chat_history.add_user_message("你好，我是赵洪欣，你是谁？")
chat_history.add_ai_message("你好，我是chatGPT，有什么可以帮到您的？")
print(chat_history)
