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
    version = models.CharField(max_length=50)
    bit = models.CharField(max_length=30)
    machine = models.CharField(max_length=50)
    PCname = models.CharField(max_length=30)
    cpu = models.CharField(max_length=50)


class attack_log(models.Model):
    attacktime = models.DateTimeField(blank=True, null=True)
    attack_ip = models.CharField(max_length=50)
    attack_way = models.CharField(max_length=30)
    log = models.FileField(upload_to='./logs/')

# class Rule(models.Model):
#     rule_id = models.IntegerField()
#     rule_name = models.CharField(max_length=128)
#     run_type = models.IntegerField(1)
#     risk = models.CharField(max_length=4)
#     priority = models.IntegerField(1)
#     filename = models.CharField(max_length=128)
#     category_id = models.IntegerField()
#     description = models.TextField(blank=True)
#     solution = models.TextField(blank=True)
#
# class Result(models.Model):
#     taskname = models.CharField()
#     rule_id = models.IntegerField()
#     risk = models.IntegerField(1)
#     url = models.URLField()
#     detail = models.TextField(blank=True)
