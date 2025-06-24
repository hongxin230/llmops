#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 2.JsonOutParser使用.py
@Time    : 2025/6/23 14:50
@Author  : zhaohongxin621@126.com
"""

import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from pydantic import BaseModel, Field

dotenv.load_dotenv()


# 1. 创建一个Json数据结构，定义Json格式
class Joke(BaseModel):
    # 冷笑话
    joke: str = Field(description="回答用户的冷笑话")
    # 冷笑话的笑点
    punchline: str = Field(description="这个冷笑话的笑点")


parser = JsonOutputParser(pydantic_object=Joke)

# 2. 构建一个提示词模板
prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答。\n{format_instructions}\n{query}").partial(
    format_instructions=parser.get_format_instructions()
)

# 3. 构建一个大预言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 4. 构建提示并进行解析
joke = parser.invoke(llm.invoke(prompt.invoke({"query": "请讲一个越野跑的冷笑话"})))

print(joke)
