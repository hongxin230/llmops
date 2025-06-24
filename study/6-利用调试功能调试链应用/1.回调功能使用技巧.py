#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.回调功能使用技巧.py
@Time    : 2025/6/24 08:28
@Author  : zhaohongxin621@126.com
"""
import time
from typing import Any, Optional, Union
from uuid import UUID

import dotenv
from langchain_core.messages import BaseMessage
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk, LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler

dotenv.load_dotenv()


class LLMOpsCallbackHandler(BaseCallbackHandler):
    start_at: float = 0

    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            tags: Optional[list[str]] = None,
            metadata: Optional[dict[str, Any]] = None,
            **kwargs: Any,
    ) -> Any:
        print("聊天模型开始执行了")
        print("serialized:", serialized)
        print("messages:", messages)
        self.start_at = time.time()

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            **kwargs: Any,
    ) -> Any:
        end_at: float = time.time()
        print("完整输出：", response)
        print("程序消耗：", end_at - self.start_at)


# 1.编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 2.创建大预言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.编排链
chain = {"query": RunnablePassthrough()} | prompt | llm | StrOutputParser()

# 5.调用链并执行
response = chain.invoke("你好，你是？", config={"callbacks": [StdOutCallbackHandler(), LLMOpsCallbackHandler()]})
print(response)
