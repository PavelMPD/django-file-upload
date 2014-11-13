# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('upload_file.views',
    url(r'^list/$', 'list', name='list'),
)
