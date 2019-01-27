#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author GoldenRoad
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [

    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^orm/', views.orm),
    url(r'^user_info/', views.user_info),
    url(r'^user_group/', views.user_group),
    # url(r'^userdetail-(<?P<nid>\d+)/', views.user_detail),
    url(r'^userdetail-(?P<nid>\d+)/', views.user_detail),
    url(r'^userdel-(?P<nid>\d+)/', views.user_del),
    url(r'^useredit-(?P<nid>\d+)/', views.user_edit),
    url(r'^orm2/', views.orm2),


]