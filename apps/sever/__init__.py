# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/18 13:03
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 13:03
"""


class RegiserSever:

    def __init__(self, app, req):
        self.app = app
        self.req = req
        self.register_global_logger()
        self.register_global_app_contexr_logger_route()
        self.register_global_health_check(self.app, self.req)

    @staticmethod
    def register_global_logger():
        """
        注册全局日志
        :return:
        """
        from apps.ext.logger.logger_config import creat_customize_log_loguru
        creat_customize_log_loguru()

    def register_global_app_contexr_logger_route(self):
        """
        注册全局日志
        :return:
        """
        # 要开启日志的激励的话，这个地方需要执行初始化化追踪的ID
        from apps.ext.logger import ContextLogerRoute
        self.app.router.route_class = ContextLogerRoute

    @staticmethod
    def register_global_health_check(app, req):
        """
        注册全局健康检查
        :return:
        """
        @app.get('/check', tags=['默认开启的健康检查'])
        async def health_check(request: req):
            from apps.ext.logger import ContextLogerRoute
            await ContextLogerRoute.async_trace_add_log_record(request, event_type='预扣库存信息222', msg='你也打好的哈')
            return 'ok242342'
