# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  app.py
@Description    :  
@CreateTime     :  2022/11/18 11:40
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 11:40
"""
from fastapi import FastAPI, Request
from apps.config.fastapi_conf import docs
from apps.sever import RegiserSever


class FastSkeletonApp:

    startge = FastAPI(
        title=docs.TITLE,
        description=docs.DESC,
        version=docs.VERSION,
        docs_url=docs.DOCS_URL,
        openapi_url=docs.OPENAPI_URL,
        redoc_url=docs.REDOC_URL,
        openapi_tags=docs.TAGS_METADATA,
        servers=docs.SERVERS,
    )

    def __init__(self):
        RegiserSever(self.startge, Request)
