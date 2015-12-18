# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20151217_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(verbose_name='Дата', default=datetime.datetime(2015, 12, 18, 17, 33, 41, 791945)),
        ),
    ]
