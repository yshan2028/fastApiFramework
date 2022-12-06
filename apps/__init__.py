# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  __init__.py
@Description    :  
@CreateTime     :  2022/11/18 11:40
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 11:40
"""
from fastapi import FastAPI, Request

# from apps.sever import RegiserSever
from starlette.middleware.cors import CORSMiddleware

from config import fastapi_conf


class FastSkeletonApp:
    app = FastAPI(
        title=fastapi_conf.TITLE,
        description=fastapi_conf.DESC,
        version=fastapi_conf.VERSION,
        docs_url=fastapi_conf.DOCS_URL,
        openapi_url=fastapi_conf.OPENAPI_URL,
        redoc_url=fastapi_conf.REDOC_URL,
        openapi_tags=fastapi_conf.TAGS_METADATA,
        servers=fastapi_conf.SERVERS,
    )

    def __init__(self):
        """
        初始化 常用的服务
        """
        self.register_global_logger()  # 注册日志处理记录初始化信息
        self.register_global_exception()  # 注册全局异常捕获信息
        self.register_global_cors()  # 全局配置跨域设置
        self.register_global_middleware()  # 注册全局中间件的注册
        self.register_global_event()  # 注册全局的启动和关闭事件
        self.register_global_ext_plugs()  # 注册所有自定义的或者第三的扩展插件

        # =====================PS=====================
        # 如果需要开启日志记录--优先级最高！必须在如有开始注册之前进行注册
        # =====================PS=====================
        self.register_global_app_contexr_logger_route()  # app注册的路由也加上日志记录
        self.register_global_health_check()  # 默认注册开启健康检测的URL检测

        # =====================PS=====================
        # 路由相关注册
        # =====================PS=====================
        self.register_global_include_routes()  # 批量导入注册路由
        self.register_global_websocket_router()  # 批量注册websocket路由

    @staticmethod
    def register_global_logger():
        """
        # 注册日志处理记录初始化信息
        :return:
        """
        # 引入函数和对应的日对象-在当前的APPS目录下建立日志收集管理目录
        from ext.logger.loger_config import creat_customize_log_loguru
        creat_customize_log_loguru()

    def register_global_exception(self):
        """
        # 注册全局异常捕踪信息
        :return:
        """
        # 引入函数和对应的日对象-在当前的APPS目录下建立日志收集管理目录
        from ext.exceptions import ApiExceptionHandler
        ApiExceptionHandler().init_app(self.app)

    def register_global_app_contexr_logger_route(self):
        """
        # app注册的路由也加上日志记录
        :return:
        """
        # 要开启日志的激励的话，这个地方需要执行初始化化追踪的ID
        from ext.logger import ContextLogerRoute
        self.app.router.route_class = ContextLogerRoute

    def register_global_health_check(self):
        """
        注册全局健康检查
        :return:
        """
        app = self.app

        @app.get('/check', tags=['默认开启的健康检查'])
        async def health_check(request: Request):
            from ext.logger import ContextLogerRoute
            await ContextLogerRoute.async_trace_add_log_record(request, event_type='预扣库存信息222', msg='你也打好的哈')
            return 'ok242342'

    def register_global_cors(self):
        """
        处理全局的跨域
        :param app:
        :return:
        """
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def register_global_middleware(self):
        """
        配置中间件
         # 中间件执行的顺序是，谁先注册,谁就再最内层，它的再后一个注册，就再最外层
        :param app:
        :return:
        """
        # from apps.middleware.global_auth import AuthMiddleware
        # self.app.add_middleware(AuthMiddleware)

        from ext.middleware.global_request import GlobalQuestyMiddleware
        self.app.add_middleware(GlobalQuestyMiddleware)

    def register_global_ext_plugs(self):
        """
        初始化第三的请求HTTP客户端对象
        """
        from ext.asynhttp import async_client
        async_client.init_app(self.app)

        # 初始化redis客户端
        # from apps.ext.pooled_postgresql import sync_pooled_postgresql_client
        # sync_pooled_postgresql_client.init_app(self.app)

        # 初始化同步redis客户端对象
        # from apps.ext.redis.syncredis2 import sync_redis_client
        # sync_redis_client.init_app(self.app)

        # 创建队列
        # sync_rabbit_client.creat_dead_exchange_and_queue()

    def register_global_include_routes(self):
        """
        导入路由模块
        :param app:
        :return:
        """
        pass

    def register_global_event(self):
        pass

    def register_global_websocket_router(self):
        pass
