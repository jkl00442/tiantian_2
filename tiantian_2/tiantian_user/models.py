# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    '''用户表'''
    # name, pwd, email, 逻辑删除
    u_name = models.CharField(max_length=20)
    u_pwd = models.CharField(max_length=40)
    u_email = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)

class UserAddress(models.Model):
    '''用户的很多收货地址'''
    # 收件人，电话，地址，邮编，邮箱，关联用户表，逻辑删除
    u_recv_name = models.CharField(max_length=20)
    u_addr = models.CharField(max_length=100)
    u_phone = models.CharField(max_length=11)
    u_zip = models.CharField(max_length=6)

    is_delete = models.BooleanField(default=False)
    u_user = models.ForeignKey(UserInfo)
