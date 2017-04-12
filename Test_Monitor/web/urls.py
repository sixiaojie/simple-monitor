"""Test_Monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import view_chart, index, add_container
urlpatterns = [
    url(r'^index/$', index),
    url(r'^chart(?P<hostname>\w*\-*\_*\w*)/$', view_chart),
    url(r'^chart/(?P<hostname>\w*\-*\_*\w*)/$', view_chart),
    url(r'^add_container', add_container),
]
