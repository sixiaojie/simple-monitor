#!/usr/bin/env python
#coding:utf-8
import os, commands, platform
from importlib import import_module

def module_install(module='MySQLdb'):
    install = False
    try:
        import_module(module)
        install = True
    except ImportError:
        cmd = 'pip install %s' %module
        result = commands.getstatusoutput(cmd)
        if result[0] == 0:
            return "ok"
        else:
            return result[1]