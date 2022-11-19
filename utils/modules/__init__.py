# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2022/11/19 14:21
------------------------------------
@ModifyTime     :  
"""
import pkgutil
import sys


def import_string(import_name, silent=False):
    """
    Imports an object based on a string.  This is useful if you want to
    use import paths as endpoints or something similar.  An import path can
    be specified either in dotted notation (``xml.sax.saxutils.escape``)
    or with a colon as object delimiter (``xml.sax.saxutils:escape``).

    If `silent` is True the return value will be `None` if the import fails.

    param import_name: the dotted name for the object to import.
    param silent: if set to `True` import errors are ignored and
                   `None` is returned instead.
    :return: imported object
    """
    # force the import name to automatically convert to strings
    # __import__ is not able to handle unicode strings in the fromlist
    # if the module is a package
    import_name = str(import_name).replace(":", ".")
    try:
        try:
            __import__(import_name)
        except ImportError:
            if "." not in import_name:
                raise
        else:
            return sys.modules[import_name]

        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])
        try:
            return getattr(module, obj_name)
        except AttributeError as e:
            raise ImportError(e)

    except ImportError as e:

        print("导入异常", e)


def find_modules(import_path, include_packages=False, recursive=False):
    """
    Finds all the modules below a package.  This can be useful to
    automatically import all views / controllers so that their metaclasses /
    function decorators have a chance to register themselves on the
    application.

    Packages are not returned unless `include_packages` is `True`.  This can
    also recursively list modules but in that case it will import all the
    packages to get the correct load path of that module.

    :param import_path: the dotted name for the package to find child modules.
    :param include_packages: set to `True` if packages should be returned, too.
    :param recursive: set to `True` if recursion should happen.
    :return: generator
    """
    module = import_string(import_path)
    path = getattr(module, "__path__", None)
    if path is None:
        raise ValueError("%r is not a package" % import_path)
    basename = module.__name__ + "."
    for _importer, modname, ispkg in pkgutil.iter_modules(path):
        modname = basename + modname
        if ispkg:
            if include_packages:
                yield modname
            if recursive:
                for item in find_modules(modname, include_packages, True):
                    yield item
        else:
            yield modname


def get_modules(package="."):
    """
    获取包名下所有非__init__的模块名
    """
    import os
    modules = []
    files = os.listdir(package)
    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append(name)
            print("名称", name)

    return modules


def import_modules(package="."):
    """
    获取包名下所有非__init__的模块名
    """
    import importlib
    modules = get_modules(package)

    # 将包下的所有模块，逐个导入，并调用其中的函数
    for module in modules:
        module = importlib.import_module(module, package)
        for attr in dir(module):
            if not attr.startswith("__"):
                func = getattr(module, attr)
                func()
