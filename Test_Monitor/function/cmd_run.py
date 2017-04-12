#!/usr/bin/env python
#coding:utf-8
from Necessary import logset
logger = logset()


def run_mysql(cmd='', file=""):
    from web.helper import mysql
    cur = mysql()
    flag = False
    if not file:
        cmd = cmd.lower()
        if "drop" in cmd:
            logger.error("不允许使用删除的命令，请与管理与联系")
        else:
            cur.execute(cmd)
    else:
        try:
            if file:
                cur.execute('source %s' %file)
            else:
                cur.execute(cmd)
            flag = True
        except Exception,e:
            logger.error('mysql have mistakes when run %s' %cmd)
            logger.error(str(e))
        if not file:
            if flag:
                cur.execute('commit')
            else:
                cur.execute('rollback')
    return flag

