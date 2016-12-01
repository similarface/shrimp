# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
'''
用户资料填写
'''
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'名字', max_length=32)
    token = models.CharField(u'token', max_length=128)
    department = models.CharField(u'部门', max_length=32)
    business_unit = models.ManyToManyField(Department)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机', max_length=32)
    mobile = models.CharField(u'手机', max_length=32)
    backup_name = models.ForeignKey('self', verbose_name=u'备用联系人',blank=True,null=True,related_name='user_backup_name')
    leader = models.ForeignKey('self', verbose_name='上级领导',blank=True,null=True)
    memo = models.TextField(u'备注', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = "用户信息"
    def __unicode__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(u'部门',max_length=64, unique=True)
    memo = models.CharField(u'备注',max_length=64, blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '部门'
        verbose_name_plural = "业务线"
