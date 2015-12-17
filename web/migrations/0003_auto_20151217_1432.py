# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20151217_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 14, 32, 39, 50234), verbose_name='Дата'),
        ),
    ]
