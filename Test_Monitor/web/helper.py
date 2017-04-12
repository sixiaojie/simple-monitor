#!/usr/bin/env python
#coding:utf-8

import ConfigParser
import docker
import ConfigParser
from function.Necessary import logset,setting
logger = logset()
setting = setting()

def conf(arg, karg):
    cf = []
    try:
        for item in karg:
            cf.append(setting.get(arg, item))
    except Exception,e:
        logger.error(e.message)
        logger.error('conf函数发生错误，由于使用不正常的参数操作，使用的参数为：%s,%s' %(arg, karg))
    return cf


def docker():
    st = conf('docker', ['ip', 'port'])
    if not st:
        return None
    client = docker.Client(base_url="tcp://%s:%s" % (set[0], set[1]))
    return client


def mysql():
    import MySQLdb
    st = conf('mysql', ['host', 'port', 'user', 'password'])
    if not st:
        return None
    conn = MySQLdb.connect(host=st[0],
                           port=int(st[1]),
                           user=st[2],
                           passwd=st[3])
    return conn.cursor()


def Redis():
    import redis
    st = conf('redis', ['host', 'port'])
    conn = redis.Redis(host=st[0],
                       port=st[1])
    return conn


def cmd_sql(sql):
    cur = mysql()
    try:
        cur.execute(sql)
        return cur.fetchall()
    except Exception,e:
        logger.error(str(e))
        return False


def privileges(user, container):
    sql = "select Admin,Name from zhang.container_privilege where Username=%s;" %user
    data = cmd_sql(sql)
    if not data:
        return False
    flag = False
    for item in data:
        if item[0] == "1" and item[1] == container:
            flag = True
            break
        else:
            continue
    return flag

