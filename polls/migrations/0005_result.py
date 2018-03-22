# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180322_1848'),
    ]

    operations = [
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
    ]
