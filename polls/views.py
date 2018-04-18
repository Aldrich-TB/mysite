# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from .forms import *
import datetime
from tools import *

# from macscan.core import test
# import sys
# sys.path.append("..")

# Create your views here.
def homepage(request):
    # test(1)
    return render_to_response('homepage.html', context_instance=RequestContext(request))


def homepage2(request):
    return render_to_response('homepage2.html', context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        # 获取表单信息
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 判断用户密码是否匹配
            user = User.objects.filter(username=username, password=password)
            if user:
                response = HttpResponseRedirect('/index')
                # response.set_cookie('username', username, 3600)
                response.set_cookie('username', username)
                return response
            else:
                return HttpResponse("Incorrect username or password.")
    else:
        uf = UserForm()
    return render_to_response('user/login.html', {'uf': uf}, context_instance=RequestContext(request))


def Sign_out(request):
    response = HttpResponseRedirect('/login')
    response.delete_cookie('username')
    return response


def charts(request):
    username = request.COOKIES.get('username')
    user = User.objects.filter(username=username)
    if user:
        logs = attack_log.objects.order_by('id')
        return render_to_response('charts.html', {'username': username,'logs':logs}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def tasks(request):
    global form, task
    username = request.COOKIES.get('username', '')
    user = User.objects.filter(username=username)
    if user:
        task = File.objects.order_by('-id')
        if request.method == 'POST':
            if request.POST.has_key('del_task'):
                ids = request.POST.getlist('ids')
                print(ids)
                idstring = ','.join(ids)
                print(idstring)
                File.objects.extra(where=['id IN (' + idstring + ')']).delete()
            else:
                form = FileForm(request.POST, request.FILES)
                if form.is_valid():
                    # 获取表单数据
                    taskname = form.cleaned_data['taskname']
                    filename = form.cleaned_data['filename']
                    starttime = datetime.datetime.now()
                    endtime = starttime + datetime.timedelta(seconds=3)

                    # 数据库信息保存
                    files = File()
                    files.username = username
                    files.taskname = taskname
                    files.filename = filename
                    files.status = 3
                    files.start_time = starttime
                    files.end_time = endtime
                    files.log = '/logs/testreport.html'
                    files.save()

                    # 上传文件保存
                    path = 'polls/uploads/'
                    destination = open(path + filename.name, 'wb+')
                    for chunk in filename.chunks():
                        destination.write(chunk)
                    destination.close()
        return render_to_response('tasks.html', {'username': username, 'tasks': task},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def index(request):
    username = request.COOKIES.get('username')
    user = User.objects.filter(username=username)
    if user:
        return render_to_response('index/index.html', {'username': username}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def host(request, page_id):
    username = request.COOKIES.get('username')
    user = User.objects.filter(username=username)
    if user:
        id = int(page_id)
        if id == 1:
            return render_to_response('index/installation.html', {'username': username},
                                      context_instance=RequestContext(request))
        elif id == 2:
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    # 获取表单数据
                    email = form.cleaned_data['email']
                    name = form.cleaned_data['name']
                    message = form.cleaned_data['message']

                    # 保存至数据库
                    contact = Contact()
                    contact.email = email
                    contact.name = name
                    contact.message = message
                    contact.save()
            return render_to_response('index/contact.html', {'username': username},
                                      context_instance=RequestContext(request))
        elif id == 3:
            return render_to_response('index/author.html', {'username': username},
                                      context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/login')


def port(request):
    username = request.COOKIES.get('username')
    user = User.objects.filter(username=username)
    if user:
        portlist = Port.objects.order_by('id')
        return render_to_response('index/port.html', {'username': username, 'portlist': portlist},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def portscan(request):
    print('1')
    # 清空数据库
    Port.objects.all().delete()
    print('2')
    port_get()
    print('done')
    return HttpResponseRedirect('/scan/port')


def hardware(request):
    username = request.COOKIES.get('username')
    user = User.objects.filter(username=username)
    if user:
        system = Sysinfo.objects.order_by('id')
        return render_to_response('index/hardware.html', {'username': username, 'system': system},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def system_scan(request):
    # 清空数据库
    Sysinfo.objects.all().delete()

    sysinfo_get()
    return HttpResponseRedirect('/scan/hardware')

def report(request):
    return render_to_response('logs/report.html')

def testreport(request):
    return render_to_response('logs/testreport.html')


def Sign_up(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 验证用户是否存在
            check = User.objects.filter(username=username)
            if check:
                return HttpResponse('The user has already existed!!')
            elif len(check) == 0:
                User.objects.create(username=username, password=password)
                return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('user/sign_up.html', {'uf': uf}, context_instance=RequestContext(request))

