#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.LLM和chainmaodel的使用技巧.py
@Time    : 2025/6/23 10:09
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

ai_message = llm.invoke(prompt.invoke({"query": "现在是几点，请讲一个越野跑运动员的冷笑话"}))

print(ai_message.type)

print(ai_message.content)

print(ai_message.response_metadata)
