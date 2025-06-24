#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 3.Mode流式输出.py
@Time    : 2025/6/23 10:38
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

response = llm.stream(prompt.invoke({"query": "请简单介绍一下亚洲商学院沙漠挑战赛与越野跑的关系"}))

for chunk in response:
    print(chunk.content, flush=True, end="")
