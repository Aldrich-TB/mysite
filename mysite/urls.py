"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from polls import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.homepage, name='homepage'),
    url(r'^homepage2', views.homepage2, name='homepage2'),

    url(r'^login/', views.login, name='login'),
    url(r'^logout', views.Sign_out, name='Sign_out'),

    url(r'^index', views.index, name='index'),
    url(r'^info/(\d)$', views.host, name='info'),

    url(r'^scan/port', views.port, name='port'),
    url(r'^ports', views.portscan, name='ports'),
    url(r'^scan/hardware', views.hardware, name='hardware'),
    url(r'^systems', views.system_scan, name='systems'),

    url(r'^charts', views.charts, name='charts'),
    url(r'^tasks', views.tasks, name='tasks'),

    url(r'^logs/report.html',views.report),
    url(r'^logs/testreport.html',views.testreport),
    url(r'^regist', views.Sign_up, name='Sign_up'),
]
