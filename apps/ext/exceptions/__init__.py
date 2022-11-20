# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/18 11:29
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 11:29
"""

from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import HTTPException as FastapiHTTPException
from fastapi.exceptions import RequestValidationError
from pydantic.errors import *
from apps.ext.logger import logger
import traceback

from apps.ext.response.json_response import ParameterException, MethodnotallowedException, NotfoundException, LimiterResException, InternalErrorException, BadrequestException
from utils.singleton import Singleton


@Singleton
class ApiExceptionHandler:
    def __init__(self, app=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if app is not None:
            self.init_app(app)

    @staticmethod
    def error_map(error_type: str, field: str, msg: str = None):
        if "missing" in error_type:
            return f"缺少参数: {field}"
        elif "params" in error_type:
            return f"参数: {field}不规范，原因 {'msg' if msg is None else msg}"
        elif "not_allowed" in error_type:
            return f"参数: {field} 类型不正确，原因 {'msg' if msg is None else msg}"
        elif "type_error" in error_type:
            return f"参数: {field} 类型不合法, 原因： {'msg'  if msg is None else msg}"
        else:
            return f"出错啦，{'msg' if msg is None else msg}"

    def init_app(self, app: FastAPI):
        """
        初始化异常错误判断
        :param app:
        :return:
        """
        app.add_exception_handler(Exception, handler=self.all_exception_handler)
        # 捕获StarletteHTTPException返回的错误异常，如返回405的异常的时候，走的是这个地方
        app.add_exception_handler(StarletteHTTPException, handler=self.http_exception_handler)
        app.add_exception_handler(RequestValidationError, handler=self.validation_exception_handler)

    async def validation_exception_handler(self, request: Request, exc: RequestValidationError):
        # print("参数提交异常错误selfself", exc.errors()[0].get('loc'))
        # 路径参数错误
        # 判断错误类型
        if isinstance(exc.raw_errors[0].exc, IntegerError):
            pass
        elif isinstance(exc.raw_errors[0].exc, MissingError):
            pass
        return ParameterException(data=self.error_map(exc.errors()[0]["type"], exc.errors()[0].get("loc", ['unknown'])[-1], exc.errors()[0].get("msg")) if len(exc.errors()) > 0 else "参数解析失败")

    @staticmethod
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """
        全局的捕获抛出的HTTPException异常，注意这里需要使用StarletteHTTPException的才可以
        :param request:
        :param exc:
        :return:
        """
        # 这里全局监听了我们的所有的HTTP响应，包括了200 的也会尽到这里来！
        if exc.status_code == 405:
            return MethodnotallowedException()
        if exc.status_code == 404:
            return NotfoundException()
        elif exc.status_code == 429:
            return LimiterResException()
        elif exc.status_code == 500:
            return InternalErrorException()
        elif exc.status_code == 400:
            return BadrequestException(message=exc.detail)

    @staticmethod
    async def all_exception_handler(self, request: Request, exc: Exception):
        """
        全局的捕获抛出的HTTPException异常，注意这里需要使用StarletteHTTPException的才可以
        :param self:
        :param request:
        :param exc:
        :return:
        """
        if isinstance(exc, StarletteHTTPException) or isinstance(exc, FastapiHTTPException):
            self.http_exception_handler(request, exc)
        else:
            # 其他内部的异常的错误拦截处理
            logger.exception(exc)
            traceback.print_exc()
            return InternalErrorException()
