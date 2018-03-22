# -*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Contact

# Register your models here.
admin.site.site_header = '入侵检测与取证系统管理'
admin.site.site_title = '入侵检测与取证系统管理'

admin.site.register(Contact)
