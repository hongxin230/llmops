#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 2.Model批处理.py
@Time    : 2025/6/23 10:32
@Author  : zhaohongxin621@126.com
"""

from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now)

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

ai_messages = llm.batch([
    prompt.invoke({"query": "你好，你是谁"}),
    prompt.invoke({"query": "请讲一个关于越野跑的冷笑话"})
])

for ai_message in ai_messages:
    print(ai_message)
    print("======================")
