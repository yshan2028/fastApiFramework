# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  main.py
@Description    :  
@CreateTime     :  2022/11/18 11:36
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 11:36
"""
import uvicorn

from apps import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=9080, log_level='debug', reload=True, access_log=False, workers=1, use_colors=True)
