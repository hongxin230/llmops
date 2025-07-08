#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.缓冲窗口记忆.py
@Time    : 2025/7/8 11:43
@Author  : zhaohongxin621@126.com
"""
from operator import itemgetter

import dotenv
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

from langchain.memory import ConversationBufferWindowMemory

dotenv.load_dotenv()

memory = ConversationBufferWindowMemory(
    k=2,
    return_messages=True,
    input_key="query",
)

# 1.提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是专业的越野跑教练"),
    MessagesPlaceholder("history"),
    ("human", "{query}"),
])

# 2.创建大预言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.构建链应用
chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
) | prompt | llm | StrOutputParser()

# 4.对话命令行
while True:
    query = input("Human: ")
    if query == "exit":
        exit(0)

    chain_input = {"query": query, "history": []}
    response = chain.stream(chain_input)
    print("AI: ", flush=True, end="")
    output = ""
    for chunk in response:
        output += chunk
        print(chunk, flush=True, end="")

    memory.save_context(chain_input, {"output": output})

    print("")
    print("history: ", memory.load_memory_variables({}))
