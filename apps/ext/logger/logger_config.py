# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  logger_config.py
@Description    :  
@CreateTime     :  2022/11/18 22:02
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2022/11/18 22:02
"""
import os

from loguru import logger


def creat_customize_log_loguru():
    """
    生产的日志文件的存在路径
    """
    import os
    pro_path = os.path.join(os.getcwd(), f'logs/')
    if not pro_path:
        pro_path = os.path.split(os.path.realpath(__file__))[0]
    # 定义info_log文件名称
    log_file_path = os.path.join(pro_path, 'info_{time:YYYYMMDD}.log')
    # 定义err_log文件名称
    err_log_file_path = os.path.join(pro_path, 'error_{time:YYYYMMDD}.log')

    from sys import stdout
    LOGURU_FORMAT = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level}</level> | <bold>{message}</bold>'
    # "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>文件: {extra[filename]}</cyan> 模块: <cyan>{extra[business]}</cyan> | 方法: <cyan>{extra[func]}</cyan> | <cyan>行数: {extra[line]}</cyan> | - <level>{message}</level>"
    # 这句话很关键避免多次的写入我们的日志
    logger.configure(handlers=[{'sink': stdout, 'format': LOGURU_FORMAT}])
    # 这个也可以启动避免多次的写入的作用，但是我们的 app:register_logger:40 -无法输出
    # logger.remove()
    # 错误日志不需要压缩
    format_err = " {time:YYYY-MM-DD HH:mm:ss:SSS} | process_id:{process.id} process_name:{process.name} | thread_id:{thread.id} thread_name:{thread.name} | {level} |\n {message}"
    # enqueue=True表示 开启异步写入
    # 使用 rotation 参数实现定时创建 log 文件,可以实现每天 0 点新创建一个 log 文件输出了
    logger.add(err_log_file_path, format=format_err, rotation='00:00', encoding='utf-8', level='ERROR', enqueue=True)  # Automatically rotate too big file
    # 对应不同的格式
    format_info = " {time:YYYY-MM-DD HH:mm:ss:SSS} | process_id:{process.id} process_name:{process.name} | thread_id:{thread.id} thread_name:{thread.name} | {level} | {message}"

    # enqueue=True表示 开启异步写入
    # 使用 rotation 参数实现定时创建 log 文件,可以实现每天 0 点新创建一个 log 文件输出了
    logger.add(log_file_path, format=format_info, rotation='00:00', compression="zip", encoding='utf-8', level='INFO', enqueue=True)  # Automatically rotate too big file
