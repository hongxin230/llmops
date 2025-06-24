#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.手写Chain实现简易版本.py
@Time    : 2025/6/23 15:58
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


class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("步骤:", step)
            print("输出", input)
            print("==============")
        return input


chain = Chain(steps=[prompt, llm, parser])

print(chain.invoke({"query": "你好，你是？"}))
