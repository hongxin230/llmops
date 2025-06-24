#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.StringOutParser使用.py
@Time    : 2025/6/23 14:39
@Author  : zhaohongxin621@126.com
"""
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1. 编排提示模板
prompt = ChatPromptTemplate.from_template("{query}")

# 2. 构建大预言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3. 创建字符串解析器
parser = StrOutputParser()

# 4. 调用大预言模型并解析
content = parser.invoke(llm.invoke(prompt.invoke({"query": "你好，你是？"})))

print(content)
