# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 14:13
------------------------------------
@ModifyTime     :  
"""


def init_routes(app):
    from utils.routes import register_nestable_blueprint_for_log
    register_nestable_blueprint_for_log(app=app, project_name='apps', api_name='modules.user', key_attribute='bp')
