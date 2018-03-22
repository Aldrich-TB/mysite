# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='log',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
