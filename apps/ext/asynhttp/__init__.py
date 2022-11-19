# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 12:19
------------------------------------
@ModifyTime     :  
"""
from dataclasses import dataclass
from aiohttp import ClientSession
import traceback
import aiohttp
# 加入日志记录
from apps.ext.logger.contexr_logger_route import ContextLogerRoute
from urllib.parse import parse_qs
from fastapi import FastAPI
from utils.singleton import Singleton


@Singleton
@dataclass
class AsynClientSession:

    def __init__(self, aiohttp_session: ClientSession = None, app: FastAPI = None):
        self.session = aiohttp_session

        # 如果有APPC传入则直接的进行初始化的操作即可
        if app is not None:
            self.init_app(app)

    def init_app(self, app: FastAPI):
        self.app = app

    async def request(self, api_url, method='GET', headers={}, islogrecord=False, params=None):
        try:
            if islogrecord and not getattr(self.app.state, 'curr_request'):
                raise Exception('需传入FastapiApp对象，并需要注册全局设置请求体对象的上下文中间件')

            if not self.session:
                # 使用with会自动的关闭链接-Unclosed client session
                async with aiohttp.ClientSession() as session:
                    async with session.request(url=api_url, method=method, headers=headers, params=params) as resp:
                        # 处理抛出异常状态又
                        resp.raise_for_status()
                        if resp.status in (401, 403):
                            raise Exception("接口请求异常！401或403错误")
                        # print('resp.content_type',resp.content_type)

                        try:
                            response = await resp.json()
                        except:
                            response = await resp.text()

                        # 日志记录
                        if islogrecord and self.app:
                            info_interface = {
                                'url': api_url,
                                'method': method,
                                'headers': str(headers) if headers else '',
                                'params': parse_qs(str(params)),
                                'state_code': str(resp.status),
                                'result': response,
                            }
                            await ContextLogerRoute.async_trace_add_log_record(self.app.state.curr_request, event_type='Third party interface', msg=info_interface)

            else:
                async with self.session.request(url=api_url, method=method, headers=headers, params=params) as resp:
                    # 处理抛出异常状态又
                    resp.raise_for_status()
                    if resp.status in (401, 403):
                        raise Exception("接口请求异常！401或403错误")
                    response = await resp.json()
                    # 需要手动的进行关闭
                    await self.session.close()
            return response
        except Exception:
            traceback.print_exc()


async_client = AsynClientSession()

if __name__ == '__main__':
    from asyncio import run


    async def main():
        results = await async_client.request(api_url='http://127.0.0.1:8080/check', islogrecord=False)
        print(results)


    run(main())
