# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
class TypeInfo(models.Model):
    '''商品分类'''
    # 商品分类标题，逻辑删除
    title = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)
