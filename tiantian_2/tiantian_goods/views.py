# -*- coding:utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from tiantian_user.models import UserInfo

# Create your models here.
class TypeInfo(models.Model):
    '''商品分类'''
    # 商品分类标题，逻辑删除
    title = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
    '''商品信息'''
    # 商品名，单价，单位，库存，商品图片，商品副标题(简介)，详细介绍，评论，点击量，所属商品分类，逻辑删除
    g_name = models.CharField(max_length=40)
    g_pic = models.ImageField(upload_to='goods/')
    g_price = models.DecimalField(6, 2) # 9999.99
    g_click = models.IntegerField(default=0)
    g_unit = models.CharField(max_length=10)
    is_delete = models.BooleanField(default=False)
    g_subtitle = models.CharField(max_length=100)
    g_has = models.IntegerField(default=0)
    g_detail = HTMLField() #　富文本编辑器

    g_type = models.ForeignKey(TypeInfo)

class GoodsComment(models.Model):
    '''商品评论(外键关联)'''
    # 用户名，评论时间，评论内容，评论图片，逻辑删除
    c_name = models.ForeignKey(UserInfo)
    c_comment_time = models.DateTimeField(auto_now=True)
    c_content = models.TextField()
    c_pic = models.ImageField(upload_to='tiantian_goods/') #　用户上传图片，从网络流中读取到的数据存到给定的目录中
    is_delete = models.BooleanField(default=False)