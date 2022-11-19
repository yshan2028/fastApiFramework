# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 14:19
------------------------------------
@ModifyTime     :  
"""
from utils.modules import find_modules, import_string


def register_nestable_blueprint_for_log(app=None, project_name=None, api_name='api', scan_name='api', key_attribute='bp', hongtu='hongtu'):
    """
    自动的导入的蓝图模块
    @param hongtu:
    @param key_attribute:
    @param scan_name:
    @param api_name:
    @param app:
    @param project_name:
    """
    if not app:
        import warnings
        warnings.warn('路由注册失败,需要传入Fastapi对象实例')
        return None
    if project_name:
        # include_packages 这个设置为True很关键，它包含了 检测 对于的_init__内的属性，这个对于外层的遍历的来说很关键
        modules = find_modules(f'{project_name}.{api_name}', include_packages=True, recursive=True)
        from apps.ext.logger.contexr_logger_route import ContextLogerRoute
        for name in modules:
            module = import_string(name)
            # 只找某个模块开始的，避免无意义的其他扫描
            if not name.endswith(scan_name):
                continue

            if hasattr(module, key_attribute):
                # apps.register_blueprint(module.mmpbp)
                # lantu = getattr(module,key_attribute)
                router = getattr(module, key_attribute)
                # 已经全局挂载还需要吗？
                # router.route_class = ContextLogerRoute
                app.include_router(router)
                # apps.register_blueprint(getattr(module,key_attribute))
            if hasattr(module, hongtu): pass
            # print('符合紅土', name)
            # getattr(module, hongtu).register(lantu)

    else:
        import warnings
        warnings.warn('路由注册失败,外部项目名称还没定义')
