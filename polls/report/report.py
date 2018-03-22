#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fail(line):
    a = "<tr id='ft1_"
    b = "' class='none'><td class='failCase'><div class='testcase'>"
    c = "</div></td><td colspan='5' align='center'><button id='btn_ft1_"
    d = "' type=\"button\"  class=\"btn btn-danger btn-xs collapsed\" data-toggle=\"collapse\" data-target='#div_ft1_"
    e = "'>失败</button><div id='div_ft1_"
    f = "' class=\"collapse\"><pre>原因： 1.没有正确过滤转义字符 2.用户输入错误的数据类型 3.数据库服务器中的漏洞 4.盲目SQL注入式攻击 5.条件响应 6.条件性差错 7.时间延误解决建议： 1.用预编译处理语言  2.轨范出错处理  3.使用专业的漏洞扫描工具</pre></div></td></tr>"
    print a + str(num) + b + line + c + str(num) + d + str(num) + e + str(num) + f


def success():
    for num in range(22,29):
        a = "<tr id = 'pt1_"
        b = "' class ='hiddenRow'><td class ='passCase'><div class ='testcase'>"
        line = "1"
        c = "</div></td><td colspan = '5' align = 'center'><span class =\"label label-success success\"> 通过 </span></td></tr>"
        print a + str(num) + b + line + c


f = open('line.txt','r')
num = 1
for line in f.readlines():
    if line == '1\n':
        success()
    else:
        fail(line)
    num = num + 1