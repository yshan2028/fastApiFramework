#!/usr/bin/evn python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   文件名称 :     auth_conf
   文件功能描述 :   功能描述
   创建人 :       小钟同学
   创建时间 :          2021/6/9
-------------------------------------------------
   修改描述-2021/6/9:         
-------------------------------------------------
"""
from functools import lru_cache
from pydantic import BaseSettings
import pprint
import secrets
from typing import List
pp = pprint.PrettyPrinter(indent=4)


class AuthUrlSettings(BaseSettings):
    # token相关-加密算法
    JWT_ALGORITHM: str = "HS256"  #
    # 秘钥生成
    # JWT_SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    JWT_SECRET_KEY: str = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
    # token配置的有效期
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3
    JWT_REFRESH_EXPIRES_DAYS: int = 1

    # 跨域设置
    ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_file_encoding = 'utf-8'

    ADMIN_WHILE_ROUTE = [
        # '/sys/doctor/logout',
        '/5gmsg/sys/doctor/login',
        '/nw/sys/doctor/login',
        '/',
        '/check',
        '/check23',
        '/jcg_admin/api/v1/login',
        '/websocket/1',
        '/openapi_url',
        '/nw/sys/doctor/login',
        '/nw/sys/doctor/loginceshi'
    ]


@lru_cache()
def get_auth_settings():
    return AuthUrlSettings()


auth_conf = get_auth_settings()
