# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from models import *
from hashlib import sha1
import datetime
from user_decorators import *

# Create your views here.
@user_login
def index(request):
    # 获取用户id
    # 根据id查找数据(用户名，联系方式，联系地址？邮箱)
    obj = UserInfo.objects.get(id = request.session['u_id'])
    context = {'title': '用户中心', 'obj': obj}
    return render(request, 'tiantian_user/info.html', context)

def register(request):
    context = {'title': '注册', 'top': '0'}
    return render(request, 'tiantian_user/register.html', context)

def handle_name(request):
    # 1.获取传来的要注册的用户名
    # 2.到数据库中查钊是否有这个用户名，
    # 2.1有，返回０
    # 2.2没有，返回１

    # 1
    name = request.GET.get('u_name')
    print(name)

    # 2.
    has = 1
    try:
        obj_list = UserInfo.objects.get(u_name = name)
        # 或
        # has = UserInfo.objects.filter(u_name = name).count()
    except Exception as e:
        print(e)
        has = 0
    else:
        has = 1

    context = {'has': has}
    return JsonResponse(context)

def handle_register(request):
    # 1.获取传来的数据，用户名，密码(加密)，邮箱
    # 1.2 对密码进行加密
    # 2.写入数据库
    # 3.写入完成后转入登陆页面

    # 1
    dict = request.POST
    name = dict.get('user_name')
    pwd = dict.get('user_pwd')
    email = dict.get('user_email')

    # 1.2
    s1 = sha1()
    s1.update(pwd)
    s_pwd = s1.hexdigest()
    print(s_pwd)

    # 2
    user = UserInfo()
    user.u_name = name
    user.u_pwd = s_pwd
    user.u_email = email
    user.save()

    # 3
    return HttpResponseRedirect('/user/login/')

def login(request):
    # 从cookie中读取用户名(如果记住用户名的话)，没有就是给它一个空字符串
    user_name = request.COOKIES.get('u_name', '')
    context = {'title': '登陆', 'top': '0', 'user_name': user_name}
    return render(request, 'tiantian_user/login.html', context)

def handle_login(request):
    # 1.获取登陆名和密码
    # 2.判断登录名是否存在
    # 3.存在
        # 3.1判断密码(加密)是否正确
            # 3.1.1密码正确
            #     返回用户中心，写入session 用户id, 用户名
            #     5.记住用户名，写入cookie或不写入并删除?
            # 3.1.2密码不正确
            #     返回登陆页面
    # 4.不存在
#     返回登陆页面

    # 1
    dict = request.POST
    name = dict.get('user_name', '')
    pwd = dict.get('user_pwd')
    print(name)
    print(pwd)

    context = {'title': '登陆', 'top': '0'}

    try:
        # 2
        user = UserInfo.objects.get(u_name = name)

        # 3.1
        s1 = sha1()
        s1.update(pwd)
        s_pwd = s1.hexdigest()

        if user.u_pwd == s_pwd:
            # 3.1.1
            request.session['u_name'] = user.u_name
            request.session['u_id'] = user.id

            # 5
            check = request.POST.get('check') #　没有check，返回None
            response = HttpResponseRedirect('/user/')
            if check:
                now_time = datetime.datetime.now()
                response.set_cookie('u_name', user.u_name, expires=now_time+datetime.timedelta(days=14))

            else:
                response.delete_cookie('u_name')

            return response
        else:
            # 3.1.2
            context['pwd_error'] = 1
            context['user_name'] = name #　错误的用户名
            return render(request, 'tiantian_user/login.html', context)

    # 4
    except Exception as e:
        print(e)
        context['name_error'] = 1
        context['user_name'] = name #　错误的用户名
        return render(request, 'tiantian_user/login.html', context)

@user_login
def order(request):
    context = {'title': '用户中心'}
    return render(request, 'tiantian_user/order.html', context)

@user_login
def site(request):
    try:
        # 获取当前地址，１个？２个？
        obj_list = UserAddress.objects.filter(u_user_id = request.session['u_id'])
        # 取第一个吧
    except Exception as e:
        print(e)
        return render(request, '404.html')
    context = {'title': '用户中心', 'list': obj_list}
    return render(request, 'tiantian_user/site.html', context)

@user_login
def handle_recv(request):
    # 1.获取传来的收件人姓名，详细地址，邮编，电话号码
    # 2.写入对应用户的地址表中
    # 3.返回这个页面

    # 1
    dict = request.POST
    name = dict.get('recv_name')
    addr = dict.get('recv_addr')
    zip = dict.get('recv_zip')
    phone = dict.get('recv_phone')

    # 2
    u_addr = UserAddress()
    u_addr.u_recv_name = name
    u_addr.u_addr = addr
    u_addr.u_phone = phone
    u_addr.u_zip = zip
    u_addr.u_user_id = request.session['u_id']
    u_addr.save()

    return HttpResponseRedirect('/user/site/')

def logout(request):
    # 1.退出当前账户
    # 2.删除用户session
    # 3.返回登陆页面
    request.session.flush()
    return HttpResponseRedirect('/user/login/')

