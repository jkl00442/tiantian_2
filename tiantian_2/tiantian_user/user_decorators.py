# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect

# 验证用户是否登陆
def user_login(fn):
    def wrapper(request, *args, **kwargs):
        if request.session.get('u_id'):
            res = fn(request, *args, **kwargs)
            return res
        else:
            return HttpResponseRedirect('/user/login/')
    return wrapper