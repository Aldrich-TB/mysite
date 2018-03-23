# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class File(models.Model):
    username = models.CharField(max_length=30)
    taskname = models.CharField(max_length=30)
    filename = models.FileField(upload_to='./uploads/')
    status = models.IntegerField()
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(blank=True, null=True)
    log = models.CharField(max_length=50)


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=300)


class Port(models.Model):
    port = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    service = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    risk = models.CharField(max_length=10)


class Sysinfo(models.Model):
    ip = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    plantform = models.CharField(max_length=50)
    version = models.CharField(max_length=300)
    bit = models.CharField(max_length=30)
    machine = models.CharField(max_length=50)
    PCname = models.CharField(max_length=30)
    cpu = models.CharField(max_length=50)


class attack_log(models.Model):
    attacktime = models.CharField(max_length=50)
    attack_ip = models.CharField(max_length=50)
    attack_way = models.CharField(max_length=30)
    log = models.CharField(max_length=50)


class Result(models.Model):
    taskname = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
