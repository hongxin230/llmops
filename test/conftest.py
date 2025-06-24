#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2025/6/16 16:03
@Author  : zhaohongxin621@126.com
"""

import pytest

from app.http.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
