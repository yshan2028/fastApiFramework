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


class RabbitSettings(BaseSettings):
    #  没有值的情况下的默认值--默认情况下读取的环境变量的值
    # 链接用户名
    RABBIT_USERNAME: str = 'guest'
    # 链接密码
    RABBIT_PASSWORD: str = 'guest'
    # 链接的主机
    RABBIT_HOST: str = 'localhost'
    # 链接端口
    RABBIT_PORT: int = 5672
    # 要链接租户空间名称
    VIRTUAL_HOST: str = 'xiaozhong'
    # 心跳检测
    RABBIT_HEARTBEAT = 5


@lru_cache()
def get_settings():
    return RabbitSettings()


# 配置实例的对象的创建
rabbitmq_conf = get_settings()
