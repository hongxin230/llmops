#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 2.LCEL表达式简化版本.py
@Time    : 2025/6/23 16:12
@Author  : zhaohongxin621@126.com
"""
from typing import Any

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()

# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

# 2.创建chain
chain = prompt | llm | parser

# 3.调用chain得到结果
print(chain.invoke({"query": "请讲一个越野跑的冷笑话"}))
