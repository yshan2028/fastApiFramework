#!/usr/bin/evn python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   文件名称 :     postgregdb
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

pp = pprint.PrettyPrinter(indent=4)


class DatabaseSettings(BaseSettings):
    DEPLOY_HOST: str = '0.0.0.0'
    DEPLOY_PORT: int = 8888
    DEPLOY_DEBUG: bool = False
    DEPLOY_RELOAD: bool = False
    DEPLOY_ACCESS_LOG: bool = False

    # 要连接的数据库名称
    DB_NAME = 'hanxuanyuyue'
    # 数据库的端口
    DB_PROT = 5432
    # 连接数据库的用户
    DB_USER = 'postgres'
    # 连接的数据库的密码
    DB_PASS = '123456'
    # 要连接的数据库的HOST
    DB_HOST = 'localhost'

    DB_MAX_CONNECTIONS = 60
    DB_STALE_TIMEOUT = 300
    DB_TIMEOUT = 20


@lru_cache()
def get_settings():
    return DatabaseSettings()


# 配置实例的对象的创建
db_conf = get_settings()
