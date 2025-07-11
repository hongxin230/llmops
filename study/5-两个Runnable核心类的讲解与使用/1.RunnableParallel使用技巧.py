#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.RunnableParallel使用技巧.py
@Time    : 2025/6/23 16:48
@Author  : zhaohongxin621@126.com
"""
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

# 1.编排prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
poem_prompt = ChatPromptTemplate.from_template("请写一篇关于{subject}的诗")

# 2.创建大预言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.创建输出解析器
parser = StrOutputParser()

# 4.编排链
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.创建并行链
map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
# map_chain = RunnableParallel({
#     "joke": joke_chain,
#     "poem": poem_chain,
# })

res = map_chain.invoke({"subject": "越野跑"})
print(res)
