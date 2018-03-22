# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_attack_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack_log',
            name='log',
            field=models.CharField(max_length=50),
        ),
    ]
