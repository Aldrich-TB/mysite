#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将样本放入列表的函数，如果列表中有了，就不重复放进去
def putInList(word, list):
    if word in list:
        return -1
    else:
        list.append(word)
        return 1


def removeInFile(normalFile, payloadFile):
    fn = open(normalFile)
    fp = open(payloadFile)
    # 正常请求列表
    listNormal = []
    # 攻击payload 列表
    listPayload = []

    # 对正常请求去重
    for line in fn.readlines():
        putInList(line, listNormal)
    # 对攻击流量去重
    for line in fp.readlines():
        putInList(line, listPayload)
    # 返回
    return {
        'normal': listNormal,
        'payload': listPayload
    }
