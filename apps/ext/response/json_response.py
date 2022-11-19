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
    api_code = 0
    # 默认Node.如果是必选的，去掉默认值即可
    result: Optional[Dict[str, Any]] = None  # 结果可以是{} 或 []
    message = '成功'
    success = True
    timestamp = int(time.time() * 1000)

    def __init__(self, success=None, http_status_code=None, api_code=None, result=None, message=None, **options):

        if result:
            self.result = result
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
            result=self.result,
            timestamp=self.timestamp,
        )

        # jsonable_encoder 处理不同字符串返回  比如时间戳 datatime类型的处理
        super(ApiResponse, self).__init__(status_code=self.http_status_code, content=jsonable_encoder(body), **options)


class BadrequestException(ApiResponse):
    http_status_code = 400
    api_code = 10031
    result = None  # 结果可以是{} 或 []
    message = '错误的请求'
    success = False


class LimiterResException(ApiResponse):
    http_status_code = 429
    api_code = 429
    result = None  # 结果可以是{} 或 []
    message = '访问的速度过快'
    success = False


class ParameterException(ApiResponse):
    http_status_code = 400
    result = {}
    message = '参数校验错误,请检查提交的参数信息'
    api_code = 10031
    success = False


class UnauthorizedException(ApiResponse):
    http_status_code = 401
    result = {}
    message = '未经许可授权'
    api_code = 10032
    success = False


class ForbiddenException(ApiResponse):
    http_status_code = 403
    result = {}
    message = '失败！当前访问没有权限，或操作的数据没权限!'
    api_code = 10033
    success = False


class NotfoundException(ApiResponse):
    http_status_code = 404
    result = {}
    message = '访问地址不存在'
    api_code = 10034
    success = False


class MethodnotallowedException(ApiResponse):
    http_status_code = 405
    result = {}
    message = '不允许使用此方法提交访问'
    api_code = 10034
    success = False


class OtherException(ApiResponse):
    http_status_code = 800
    result = {}
    message = '未知的其他HTTPEOOER异常'
    api_code = 10034
    success = False


class InternalErrorException(ApiResponse):
    http_status_code = 500
    result = {}
    message = '程序员哥哥睡眠不足，系统崩溃了！'
    api_code = 500
    success = False


class InvalidTokenException(ApiResponse):
    http_status_code = 401
    api_code = 401
    message = '很久没操作，令牌失效'
    success = False


class ExpiredTokenException(ApiResponse):
    http_status_code = 422
    message = '很久没操作，令牌过期'
    api_code = 10050
    success = False


class FileTooLargeException(ApiResponse):
    http_status_code = 413
    api_code = 413
    result = None  # 结果可以是{} 或 []
    message = '文件体积过大'


class FileTooManyException(ApiResponse):
    http_status_code = 413
    message = '文件数量过多'
    api_code = 10120
    result = None  # 结果可以是{} 或 []


class FileExtensionException(ApiResponse):
    http_status_code = 401
    message = '文件扩展名不符合规范'
    api_code = 10121
    result = None  # 结果可以是{} 或 []


class Success(ApiResponse):
    http_status_code = 200
    api_code = 20000
    result = None  # 结果可以是{} 或 []
    message = '自定义成功返回'
    success = True


class Fail(ApiResponse):
    http_status_code = 200
    api_code = 20110
    result = None  # 结果可以是{} 或 []
    message = '自定义成功返回'
    success = False
