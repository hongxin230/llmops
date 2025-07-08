#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 文件对话历史消息组件.py
@Time    : 2025/7/7 12:32
@Author  : zhaohongxin621@126.com
"""

import dotenv

from openai import OpenAI
from langchain_community.chat_message_histories import FileChatMessageHistory

chat_history = FileChatMessageHistory("./memory.txt")

dotenv.load_dotenv()

client = OpenAI(base_url='https://yibuapi.com/v1')

while True:
    query = input("Human: ")

    if query == "exit":
        exit(0)

    print("AI: ", flush=True, end="")

    system_prompt = (
        "你是OpenAI开发的ChatGPT聊天机器人，可以根据响应的上下文回复用户信息，上下文里存放的是人类与你对话的信息列表，"
        f"<content>{chat_history}<content>\n\n"
    )

    response = client.chat.completions.create(
        model='gpt-4-turbo',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        stream=True,
    )
    ai_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
        print(content, flush=True, end="")

    chat_history.add_user_message(query)
    chat_history.add_ai_message(ai_content)
    print("")
