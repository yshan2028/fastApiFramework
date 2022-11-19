# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  global_request.py
@Description    :  
@CreateTime     :  2022/11/19 12:05
------------------------------------
@ModifyTime     :  
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class GlobalQuestyMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # 给当前的app这是当前的请求上下文对象
        request.app.state.curr_request = request
        response = await call_next(request)
        # 请求之后响应体
        return response
