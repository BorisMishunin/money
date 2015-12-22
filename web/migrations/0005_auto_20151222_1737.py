# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0004_auto_20151218_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='author',
            field=models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(verbose_name='Дата', default=datetime.datetime(2015, 12, 22, 17, 37, 11, 23817)),
        ),
    ]
