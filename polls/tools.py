#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *
import platform
import socket
import nmap

risk_port = [15, 21, 22, 23, 25, 53, 80, 135, 137, 138, 139, 161, 1099, 1433, 1521, 3306, 3389, 8080]


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def sysinfo_get():
    sys = Sysinfo()
    sys.ip = get_host_ip()
    sys.system = platform.system()
    sys.plantform = platform.platform()
    sys.version = platform.version()
    sys.bit = platform.architecture()
    sys.machine = platform.machine()
    sys.PCname = platform.node()
    sys.cpu = platform.processor()
    sys.save()


def port_get():
    host = '127.0.0.1'
    nm = nmap.PortScanner()
    nm.scan(host, '0-65535')

    # 提取扫描信息 分类
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            state = nm[host][proto][port]['state']
            name = nm[host][proto][port]['name']
            product = nm[host][proto][port]['product']
            if product == "":
                product = 'unknown'
            if port in risk_port:
                risk = 'risk'
            else:
                risk = 'safe'

            # 保存至数据库
            portlist = Port()
            portlist.port = str(port) + '/' + str(proto)
            portlist.state = state
            portlist.service = name
            portlist.product = product
            portlist.risk = risk
            portlist.save()
