# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 14:13
------------------------------------
@ModifyTime     :  
"""


def modeles_routes(app):
    from .user import init_routes as user_routes
    user_routes(app=app)
