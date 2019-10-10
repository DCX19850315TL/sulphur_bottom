# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 10, 9, 55, 15, 435000), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
