# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 23:37
# @Author  : Zheng Xingtao
# @File    : urls.py


from django.urls import path

from wow.item import views

app_name = "item"

urlpatterns = [
    path("all/", views.ItemsListView.as_view(), name="items"),
]
