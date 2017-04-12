#!/usr/bin/env python
import docker
import ConfigParser


def Client():
    setting = ConfigParser.ConfigParser()
    setting.read('docker.conf')
    host = setting.get('docker', 'ip')
    port = setting.get('docker', 'port')
    client = docker.Client(base_url="tcp://%s:%s" % (host, port))
    return client

