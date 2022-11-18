# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/18 11:37
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 11:37
"""
from apps.app import FastSkeletonApp


def create_app():
    """
    创建我们的Fastapi对象
    :return:
    """
    apps = FastSkeletonApp()
    # 返回fastapi的App对象
    return apps.startge
