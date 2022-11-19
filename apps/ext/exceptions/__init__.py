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
from apps.ext.response.json_response import *
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

    def init_app(self, app: FastAPI):

        # @app.exception_handler(StarletteHTTPException)
        # @app.exception_handler(RequestValidationError)
        # @app.exception_handler(Exception)
        app.add_exception_handler(Exception, handler=self.all_exception_handler)
        # 捕获StarletteHTTPException返回的错误异常，如返回405的异常的时候，走的是这个地方
        app.add_exception_handler(StarletteHTTPException, handler=self.http_exception_handler)
        app.add_exception_handler(RequestValidationError, handler=self.validation_exception_handler)

    @staticmethod
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # print("参数提交异常错误selfself", exc.errors()[0].get('loc'))
        # 路径参数错误
        # 判断错误类型
        if isinstance(exc.raw_errors[0].exc, IntegerError):
            pass
        elif isinstance(exc.raw_errors[0].exc, MissingError):
            pass
        return ParameterException(http_status_code=400, api_code=400, message='参数校验错误', result={
            "detail": exc.errors(),
            "body": exc.body
        })

    @staticmethod
    async def all_exception_handler(request: Request, exc: Exception):
        """
        全局的捕获抛出的HTTPException异常，注意这里需要使用StarletteHTTPException的才可以
        :param request:
        :param exc:
        :return:
        """
        # log_msg = f"捕获到系统错误：请求路径:{request.url.path}\n错误信息：{traceback.format_exc()}"
        if isinstance(exc, StarletteHTTPException) or isinstance(exc, FastapiHTTPException):
            if exc.status_code == 405:
                return MethodnotallowedException()
            if exc.status_code == 404:
                return NotfoundException()
            elif exc.status_code == 429:
                return LimiterResException()
            elif exc.status_code == 500:
                return InternalErrorException()
            elif exc.status_code == 400:
                # 有部分的地方直接的选择使用raise的方式抛出了异常，这里也需要进程处理
                # raise HTTPException(HTTP_400_BAD_REQUEST, 'Invalid token')
                return BadrequestException(msg=exc.detail)

            return BadrequestException()
        else:
            # 其他内部的异常的错误拦截处理
            logger.exception(exc)
            traceback.print_exc()
            return InternalErrorException()

    @staticmethod
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        '''
           全局的捕获抛出的HTTPException异常，注意这里需要使用StarletteHTTPException的才可以
           :param request:
           :param exc:
           :return:
           '''
        # 这里全局监听了我们的所有的HTTP响应，包括了200 的也会尽到这里来！
        # print("撒很好收到哈搜地和撒谎的撒22222222222===========",exc)
        # log_msg = f"捕获到系统错误：请求路径:{request.url.path}\n错误信息：{traceback.format_exc()}"

        if exc.status_code == 405:
            return MethodnotallowedException()
        if exc.status_code == 404:
            return NotfoundException()
        elif exc.status_code == 429:
            return LimiterResException()
        elif exc.status_code == 500:
            return InternalErrorException()
        elif exc.status_code == 400:
            # 有部分的地方直接的选择使用raise的方式抛出了异常，这里也需要进程处理
            # raise HTTPException(HTTP_400_BAD_REQUEST, 'Invalid token')
            return BadrequestException(msg=exc.detail)
