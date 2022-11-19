# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  json_response.py
@Description    :  
@CreateTime     :  2022/11/19 12:30
------------------------------------
@ModifyTime     :  
"""
from typing import Any, Dict, Optional

# 自定义返回的错误的响应体信息
# ORJSONResponse一依赖于：orjson
from fastapi.responses import JSONResponse

import time
from fastapi.encoders import jsonable_encoder


class ApiResponse(JSONResponse):
    # 定义返回响应码--如果不指定的话则默认都是返回200
    http_status_code = 200
    # 默认成功
    api_code = 20000
    # 默认Node.如果是必选的，去掉默认值即可
    data: Optional[Dict[str, Any]] = None  # 结果可以是{} 或 []
    message = '请求成功'
    success = True
    timestamp = int(time.time() * 1000)

    def __init__(self, success=None, http_status_code=None, api_code=None, data=None, message=None, **options):

        if data:
            self.data = data
        if message:
            self.message = message

        if api_code:
            self.api_code = api_code

        if success is not None:
            self.success = success

        if http_status_code:
            self.http_status_code = http_status_code

        # 返回内容体
        body = dict(
            message=self.message,
            code=self.api_code,
            success=self.success,
            data=self.data,
            timestamp=self.timestamp,
        )

        # jsonable_encoder 处理不同字符串返回  比如时间戳 datatime类型的处理
        super(ApiResponse, self).__init__(status_code=self.http_status_code, content=jsonable_encoder(body), **options)


class BadrequestException(ApiResponse):
    http_status_code = 400  # 错误的请求
    api_code = 20030
    data = None  # 结果可以是{} 或 []
    message = '错误的请求'
    success = False


class LimiterResException(ApiResponse):
    http_status_code = 429  # 请求太多
    api_code = 20032
    data = None  # 结果可以是{} 或 []
    message = '访问的速度过快'
    success = False


class ParameterException(ApiResponse):
    http_status_code = 400  # 参数错误的请求
    api_code = 20031  # 参数错误, 'Params error'
    data = {}
    message = '参数校验错误,请检查提交的参数信息'
    success = False


class UnauthorizedException(ApiResponse):
    http_status_code = 401  # 未经授权
    api_code = 20001  # 无效的token, 'Invalid token'
    data = {}
    message = '未经许可授权'
    success = False


class ForbiddenException(ApiResponse):
    http_status_code = 403  # 禁止访问
    api_code = 20033  # 访问地址失败
    data = {}
    message = '失败！当前访问没有权限，或操作的数据没权限!'
    success = False


class NotfoundException(ApiResponse):
    http_status_code = 404  # 没找到
    api_code = 20034  # 访问不存在
    data = {}
    message = '访问地址不存在'
    success = False


class MethodnotallowedException(ApiResponse):
    http_status_code = 405  # 方法不允许
    api_code = 20035
    data = {}
    message = '不允许使用此方法提交访问'
    success = False


class OtherException(ApiResponse):
    http_status_code = 400  # 未知错误的请求
    api_code = 99999
    data = {}
    message = '未知的其他HTTPEOOER异常'
    success = False


class InternalErrorException(ApiResponse):
    http_status_code = 500
    api_code = 20500
    data = {}
    message = '程序员哥哥睡眠不足，系统崩溃了！'
    success = False


class InvalidTokenException(ApiResponse):
    http_status_code = 401  # 未经授权
    api_code = 20002  # 无效的token, 'Invalid token'
    message = '很久没操作，令牌失效'
    success = False


class ExpiredTokenException(ApiResponse):
    http_status_code = 422  # 令牌过期
    api_code = 20003  # access token过期, 'Access token expired'
    message = '很久没操作，令牌过期'
    success = False


class FileTooLargeException(ApiResponse):
    http_status_code = 413  # 请求包太大
    api_code = 20023
    data = None  # 结果可以是{} 或 []
    message = '文件体积过大'


class FileTooManyException(ApiResponse):
    http_status_code = 413
    message = '文件数量过多'
    api_code = 20024
    data = None  # 结果可以是{} 或 []


class FileExtensionException(ApiResponse):
    http_status_code = 401
    message = '文件扩展名不符合规范'
    api_code = 20025
    data = None  # 结果可以是{} 或 []


class Success(ApiResponse):
    http_status_code = 200
    api_code = 20000
    data = None  # 结果可以是{} 或 []
    message = '请求成功'
    success = True


class Fail(ApiResponse):
    http_status_code = 200
    api_code = 20110
    data = None  # 结果可以是{} 或 []
    message = '请求失败'
    success = False
