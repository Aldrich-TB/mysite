# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attack_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attacktime', models.CharField(max_length=50)),
                ('attack_ip', models.CharField(max_length=50)),
                ('attack_way', models.CharField(max_length=30)),
                ('log', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('taskname', models.CharField(max_length=30)),
                ('filename', models.FileField(upload_to=b'./uploads/')),
                ('status', models.IntegerField()),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('log', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('port', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=10)),
                ('service', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=30)),
                ('risk', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskname', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sysinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=50)),
                ('system', models.CharField(max_length=50)),
                ('plantform', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('bit', models.CharField(max_length=30)),
                ('machine', models.CharField(max_length=50)),
                ('PCname', models.CharField(max_length=30)),
                ('cpu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
