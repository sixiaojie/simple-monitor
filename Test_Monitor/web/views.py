#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render, render_to_response
# Create your views here.
import json
import collections
from function.Necessary import logset
from helper import mysql, Redis,privileges
from django.utils.safestring import mark_safe

logger = logset()
def color(data):
    if data == "success" or data == "ok":
        data = "<a style='color:green'>%s</a>" % data
    elif data == "failed" or data == "fail":
        data = "<a style='color:red'>%s</a>" % data
    elif data == "unusual" or data == "unusuals":
        data = "<a style='color:#660000'>%s</a>" % data
    elif data == "unknown" or data == "unknowns":
        data = "<a style='color:ffff00'>%s</a>" % data
    return data


def index(request):
    try:
        all_data = []
        host_list = {}
        cur = mysql()
        cur.execute('select H_id,hostname,IP,System from zhang.hostname')
        val = cur.fetchall()
        cur.execute("select hostname_id,service_name,status,DATE_FORMAT(time,'%Y-%m-%d %H:%i:%s') from zhang.service order by id")
        service = cur.fetchall()
        host_all = []
        for key in val:
            host_all.append(key[1])
            host_list[key[0]] = key[1]
        i = 0
        list = {}
        for key in service:
            service_list = []
            status = mark_safe(color(key[2]))
            if host_list[key[0]] in list:
                id = list[host_list[key[0]]]
                data = [key[1], status, key[3]]
                all_data[id][2].append(data)
            else:
                data = []
                list[host_list[key[0]]] = i
                if i%2 == 0:
                    data = [host_list[key[0]], True, [[key[1], status, key[3]]]]
                else:
                    data = [host_list[key[0]], False, [[key[1], status, key[3]]]]
                all_data.append(data)
                i += 1
    except Exception,e:
        print str(e)
        val = [['error', 'error', 'error', 'error']]
    try:
        cur.close()
    except Exception,e:
        logger.error('数据库连接failed')
    #return render_to_response('index/index.html')
    return render_to_response('monitor.html', {'data': val, 'service': all_data})

def usage(name):
    if name == "Mysql":
        return "连接数"
    elif name == "disk" or name == "Memory":
        return "使用量%"


def view_chart(request, hostname):
    print hostname
    if not hostname:
        hostname = 'LAMP'
    try:
        service = []
        chart_data = collections.OrderedDict()
        monitor = {}
        cur = mysql()
        redis = Redis()
        cur.execute('select H_id,ip from zhang.hostname where hostname="%s"' % hostname)
        host = cur.fetchone()
        print host
        if len(host) == 2:
            host_id = host[0]
            ip = host[1]
            data = redis.get(hostname)
            if not data:
                raise KeyError
            data = json.loads(data)
            for key, name in data.items():
                key = key.encode('utf-8')
                monitor = collections.OrderedDict()
                for item in name:
                    item = item.encode('utf-8')
                    service.append(item)
                    sql1 = "select Monitor_data,date_format(time,'%H:%m:%s') "
                    sql2 = "from zhang.%s where Name='%s' and hostname_id = %d order by id desc limit 10" % (key, item, host_id)
                    sql = sql1 + sql2
                    cur.execute(sql)
                    data1 = cur.fetchall()
                    list_count = []
                    time_list = []
                    for count in data1:
                        list_count.append(int(count[0]))
                        time_list.append(count[1])
                    val = usage(key)
                    monitor[item] = [time_list, list_count,val]
                chart_data[key] = monitor
        else:
            print "can't find the host %s" %hostname
            raise KeyError
        return render_to_response('test.html', {'data': chart_data, 'service': service,'ip':ip})
    except Exception,e:
        print str(e)
        cur.close()
        return HttpResponse('failed')


def add_container(request):
    if request.method == 'POST':
        list_info = request.POST.dict()
        print list_info
        return HttpResponse('ok')
    else:
        return render_to_response('form.html')


def add_user(request):
    cur = mysql()
    try:
        user = request.session['is_backend_login']['user']
        if request.method == 'POST':
            print "这里下写下方法"
        else:
            cur.execute('select Name from zhang.container;')
            return_data = []
            data = cur.fetchall()
            for item in data:
                return_data.append(item[0][0])
            return render_to_response('test.html', {'data': return_data})
    except Exception,e:
        return redirect('/backend/login')


def container_privilege(requset):
    try:
        user = requset.session['is_backend_login']['user']
        cur = mysql()
        if requset.method == 'POST':
            container = requset.POST.get('container')
            data = privileges(user,container)
            if not data:
                return HttpResponse('你没有权限，请找%s的管理员' %container)
            print "............"
            print "这里写方法:用户名，权限，使用时间。判断的方法：获取当前创建的用户的人的账号是不是管理员，若是的，无所谓，若不是，那么就看该人对当前使用的容器是不是管理员的身份"
        else:
            cur.execute('select Name from zhang.container;')
            containers = cur.fetchall()
            all_container = []
            for item in containers:
                all_container.append(item[0])
            return render_to_response('containers.html', {'data': all_container})
    except Exception,e:
        return redirect('/backend/login')