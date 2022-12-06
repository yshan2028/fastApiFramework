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

from apps import FastSkeletonApp


def create_app():
    '''
    创建我们的Fastapi对象
    :return:
    '''
    # from apps.middleware.logroute import ContextIncludedRoute
    # self.app.router.route_class = ContextIncludedRoute

    startge = FastSkeletonApp()
    # 返回fastapi的App对象
    return startge.app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=9080, log_level='debug', reload=True, access_log=True, workers=1, use_colors=True)
