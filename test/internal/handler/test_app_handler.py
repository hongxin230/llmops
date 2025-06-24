#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : test_app_handler.py
@Time    : 2025/6/16 15:55
@Author  : zhaohongxin621@126.com
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:

    @pytest.mark.parametrize("query", [None, "你好，你是?"])
    def test_completion(self, query, client):
        r = client.post("/app/completion", json={"query": query})
        assert r.status_code == 200
        if query is None:
            assert r.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert r.json.get("code") == HttpCode.SUCCESS
        print("响应内容：", r.json)
