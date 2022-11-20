# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 14:14
------------------------------------
@ModifyTime     :  
"""
from typing import Union

from pydantic import BaseModel

from apps.ext.response.json_response import Success
from apps.modules.user.api import bp as lantu


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@lantu.get('/list', summary='用户列表')
def user_list():
    data = {
        'name': '张三'
    }
    return Success(data=data)


@lantu.post('/add', summary='用户列表')
def user_add(item: Item):
    return Success(data=item)
