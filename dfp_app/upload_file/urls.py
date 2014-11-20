# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('upload_file.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^file_list/$', 'file_list', name='file_list'),
    url(r'^ajax-upload/$', 'json_upload', name='json_upload'),
)
