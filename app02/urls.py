#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author GoldenRoad
from django.conf.urls import url
from django.contrib import admin
from app02 import views
urlpatterns = [
    url(r'^login/', views.login),


]