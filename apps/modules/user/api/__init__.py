# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 14:14
------------------------------------
@ModifyTime     :  
"""
from fastapi import APIRouter

from apps.ext.logger import ContextLogerRoute

bp = APIRouter(tags=['用户相关'], prefix='/user/api/v1', route_class=ContextLogerRoute)