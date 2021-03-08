# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 23:35
# @Author  : Zheng Xingtao
# @File    : tests.py


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """自定义用户模型"""
    nickname = models.CharField(null=True, blank=True, max_length=255, verbose_name='昵称')
    job_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='职称')
    introduction = models.TextField(blank=True, null=True, verbose_name='简介')
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='头像')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name = "用户"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_profile_name(self):
        if self.nickname:
            return self.nickname
        return self.username
