#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : app_handler.py
@Time    : 2025/6/12 10:50
@Author  : zhaohongxin621@126.com
"""

import os
import uuid
from dataclasses import dataclass
from uuid import UUID
from flask import request
from injector import inject
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validation_error_json, success_message
from langchain_core.prompts import ChatPromptTemplate, prompt
from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的App记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，删除的名字是{app.name}")

    def debug(self, app_id: UUID):
        """聊天接口"""
        # 1.提取从接口中获取的输入
        req = CompletionReq()
        if not req.validate():
            return validation_error_json(req.errors)

        # 2.构建组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
        parser = StrOutputParser()

        # 3.构建chain
        chain = prompt | llm | parser
        # 4.执行chain
        content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}
