#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import urllib
import fileinput

ip_re = r"?P<ip>[\d.]*"
date_re = r"?P<date>\d+"
month_re = r"?P<month>\w+"
year_re = r"?P<year>\d+"
time_re = r"?P<time>\S+"
method_re = r"?P<method>\S+"
request_re = r"?P<request>\S+"
status_re = r"?P<status>\d+"
bodyBytesSent_re = r"?P<bodyBytesSent>\d+"


def parserequest(log):
    p = re.compile(r"/\?id\=(%s)" % request_re, re.VERBOSE)
    s = re.findall(p, log)
    key = ''.join(s)
    return urllib.unquote(key)


def month_change(argument):
    return{
        'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
        'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12,
    }.get(argument,99)


for log in fileinput.input(["E:\\mysite\\polls\\logs\\access_log1.txt"]):
    p = re.compile(r"(%s)\ -\ -\ \[(%s)/(%s)/(%s)\:(%s)\ [\S]+\]\ \"(%s)?[\s]?(%s)?.*?\"\ (%s)\ (%s)" % (ip_re, date_re, month_re, year_re, time_re, method_re, request_re, status_re, bodyBytesSent_re), re.VERBOSE)
    pr = re.findall(p, log)
    # print pr

    [(ip,date,month,year,Time,method,request,status,bodyBytesSent)] = pr

    time_str = '%s%s%s %s' %(year, month, date, Time)
    # print time.strptime(time_str, '%Y%b%d %H:%M:%S')
    print parserequest(request)