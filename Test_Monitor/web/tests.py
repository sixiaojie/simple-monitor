from django.test import TestCase

# Create your tests here.
import docker
d = docker.Client(base_url='tcp://192.168.13.132', version='1.24')
