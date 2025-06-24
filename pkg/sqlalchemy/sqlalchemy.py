#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : sqlalchemy.py
@Time    : 2025/6/18 11:21
@Author  : zhaohongxin621@126.com
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):

    @property
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
