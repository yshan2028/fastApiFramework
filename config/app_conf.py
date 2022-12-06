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

pp = pprint.PrettyPrinter(indent=4)


class AppSettings(BaseSettings):
    # 用户允许下单的间隔时间：单位秒
    APP_USERR_ORDER_PAY_LIMT_TIME_JG: int = 3
    # 用户一天允许下单操操作总次数频次
    APP_USERR_ORDER_PAY_LIMT_TIME_ALL_TIME: int = 60 * 60 * 24  #
    APP_USERR_ORDER_PAY_LIMT_TIMES_ALL_ACTION: int = 50  #


@lru_cache()
def get_app_settings():
    return AppSettings()


app_settings = get_app_settings()
