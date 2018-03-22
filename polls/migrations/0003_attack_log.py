# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180320_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='attack_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attacktime', models.CharField(max_length=50)),
                ('attack_ip', models.CharField(max_length=50)),
                ('attack_way', models.CharField(max_length=30)),
                ('log', models.FileField(upload_to=b'./logs/')),
            ],
        ),
    ]
