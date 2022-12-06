#!/usr/bin/evn python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   文件名称 :     redis_conf
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
from pydantic import AnyUrl, BaseSettings
import os

pp = pprint.PrettyPrinter(indent=4)


class RedisSettings(BaseSettings):
    #  没有值的情况下的默认值--默认情况下读取的环境变量的值
    HOST: str = '127.0.0.1'
    PORT: int = 6379
    PASSWORD: str = ''
    DEPLOY_DEBUG: bool = False
    DEPLOY_RELOAD: bool = False
    DEPLOY_ACCESS_LOG: bool = False

    # redis://:root12345@127.0.0.1:6379/0?encoding=utf-8
    # 下面这个其实不需要这么操作，默认会自己去读取环境变量的值
    redis_url: AnyUrl = os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/0?encoding=utf-8")
    redis_password: str = os.getenv("REDIS_PASSWORD", "")
    redis_db: int = int(os.getenv("REDIS_DB", "0"))

    # 哨兵机制的链接的配置
    use_redis_sentinel: bool = (
        True if os.getenv("REDIS_USE_SENTINEL", "0") == "1" else False
    )
    redis_sentinel_port: int = int(os.getenv("REDIS_SENTINEL_PORT", "26379"))
    redis_sentinel_url: str = os.getenv("REDIS_SENTINEL_URL", "")
    redis_sentinel_password: str = os.getenv("REDIS_SENTINEL_PASSWORD", "")
    redis_sentinel_master_name: str = os.getenv(
        "REDIS_SENTINEL_MASTER_NAME", "molmaster"
    )


@lru_cache()
def get_settings():
    return RedisSettings()


# 配置实例的对象的创建
redis_conf = get_settings()
