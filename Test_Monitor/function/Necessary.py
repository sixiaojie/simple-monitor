#!/usr/bin/env python
#coding:utf-8
import logging
import platform
import ConfigParser

def logset():
    os = platform.system()
    if os == "Linux":
        filename = '/var/log/auto/message'
    elif os == 'Windows':
        filename = 'E:\\temp\\error.log'
    else:
        print '不支持%s系统' %os
        exit(4)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a,%d %b %Y %H:%M:%S',
                        filename='G:\\temp\\error.log',
                        filemode='a',)
    return logging


def setting():
    import os
    import sys
    if os.path.exists('acquire.conf'):
        logset().info('直接读取成功')
        st = ConfigParser.ConfigParser()
        st.read("acquire.conf")
    else:
        logset().warn('直接读取失败，使用路径式读取')
        path = sys.path[0]
        print path
        path = os.getcwd()
        print path
        os1 = platform.system()
        print os1
        if os1 == 'Linux':
            file = path+'/'+'acquire.conf'
        else:
            file = path+'\\'+'acquire.conf'
        print file
        if os.path.exists(file):
            logset().info('路径式读取成功')
            st = ConfigParser.ConfigParser()
            st.read(file)
        else:
            logset().error('直接和路径式失败')
            print "read conf file is failed"
            exit(3)
    return st


def check_mysql():
    '''#####模块的安装########'''
    import check, os
    result = check(module='MySQLdb')
    if result == 'ok':
        print "module MySQLdb is already installed or install successfully"
    else:
        logset().error(result)
        print result
        exit(9)
    '''#####创建所需的表#######'''
    import cmd_run
    path = os.getcwd()
    os = platform.system()
    if os == "Linux":
        file = path+'/'+'a.sql'
    else:
        file = path+'\\'+'a.sql'

