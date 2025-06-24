#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 2.RunnableParallel模拟检索.py
@Time    : 2025/6/23 17:02
@Author  : zhaohongxin621@126.com
"""
import dotenv
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()


def retrieval(query: str) -> str:
    """一个模拟的检索器函数"""
    print("正在检索")
    return "我是慕小课"


# 1.编排prompt
prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行生成
<context>
{context}
</context>

用户的提问是：{query}

""")

# 2.构建大预言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.输出解析器
parser = StrOutputParser()

# 4.构建链
chain = {
            "context": lambda x: retrieval(x["query"]),
            "query": itemgetter("query"),
        } | prompt | llm | parser

# 5.调用链
content = chain.invoke({"query": "你好，我是谁？"})

print(content)
