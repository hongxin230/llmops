#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : 1.摘要缓冲混合记忆.py
@Time    : 2025/7/4 15:15
@Author  : zhaohongxin621@126.com
"""
from typing import Any

import dotenv
from openai import OpenAI

dotenv.load_dotenv()


# 1.max_tokens用于判断是否生成新的摘要

# 2.summary存储摘要的信息

# 3.chat_histories存储历史对话

# 4.计算传入文本的token数

# 5.存储新的交流对话

# 6.get_buffer_string用于将历史对话转换成字符串

# 7.load_memory_variables用于加载记忆变量信息

# 8.summary_text用于将旧的摘要和传入的对话生成新的摘要
class ConversationSummaryBufferMemory:
    """摘要缓冲混合记忆类"""

    def __init__(self, summary: str = '', chat_histories: list = None, max_tokens: int = 300):
        self.summary = summary
        self.chat_histories = [] if chat_histories is None else chat_histories
        self.max_tokens = max_tokens
        self._client = OpenAI(base_url='https://yibuapi.com/v1')

    @classmethod
    def get_num_tokens(cls, query: str) -> int:
        """计算传入的query的token数"""
        return len(query)

    def save_content(self, human_query: str, ai_content: str) -> None:
        """保存传入的新一次对话信息"""
        self.chat_histories.append({"human": human_query, "ai": ai_content})
        buffer_string = self.get_buffer_string()
        tokens = self.get_num_tokens(buffer_string)
        if tokens > self.max_tokens:
            first_char = self.chat_histories[0]
            print("新摘要生成中...")
            self.summary = self.summary_text(self.summary,
                                             f"Human: {first_char.get('human')}\nAI: {first_char.get('ai')}")
            print("新摘要生成成功:", self.summary)

            del self.chat_histories[0]

    def get_buffer_string(self) -> str:
        """将历史对话转换成字符串"""
        buffer: str = ''
        for chat in self.chat_histories:
            buffer += f"{chat.get('human')} {chat.get('ai')}"
        return buffer.strip()

    def load_memory_variables(self) -> dict[str, Any]:
        """加载记忆变量为一个字典，便于格式化到prompt中"""
        buffer_string = self.get_buffer_string()
        return {
            "chat_history": f"摘要：{self.summary}\n\n 历史信息: {buffer_string}\n\n",
        }

    def summary_text(self, origin_summary: str, new_line: str) -> str:
        """用于将旧摘要和传入的新对话生成一个新摘要"""

        prompt = f"""你是一个强大的聊天机器人，请根据用户提供的谈话内容，总结摘要，并将其添加到先前提供的摘要中，返回一个新的摘要，如果用户的对话信息包含姓名、性别、重要事件等信息，这些信息都要包含在生成的摘要中，摘要尽可能要还原用户的对话记录。

<example>
当前摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向上的力量

新的对话：
Human：你为什么认为人工智能是一股向上的力量？
AI：因为人工智能会帮助人类充分发挥潜力。

新的摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向上的力量，因为它会帮助人类充分发挥潜力。

</example>

==============以下的数据是实际需要处理的数据=============
当前摘要：{origin_summary}
新的对话：
{new_line}
请帮用户生成新摘要："""
        completion = self._client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content


# 1.创建客户端
client = OpenAI(base_url='https://yibuapi.com/v1')
memory = ConversationSummaryBufferMemory("", [], 300)

# 2.创建人机对话
while True:
    # 3.获取人类输入
    query = input('Human:')

    # 4.退出
    if query == 'q':
        break

    memory_variables = memory.load_memory_variables()
    answer_prompt = (
        "你是一个越野跑专家，请根据用户输入回答问题。 \n\n"
        f"{memory_variables.get('chat_history')} \n\n"
        f"用户的提问是：{query}"
    )

    response = client.chat.completions.create(
        model='gpt-4-turbo',
        messages=[
            {"role": "user", "content": answer_prompt},
        ],
        stream=True,
    )

    print("AI: ", flush=True, end="")

    ai_content = ''
    for trunk in response:
        if trunk.choices and len(trunk.choices) > 0:
            content = trunk.choices[0].delta.content
            if content is None:
                break
            ai_content += content
            print(content, flush=True, end="")
    print("")
    memory.save_content(query, ai_content)
