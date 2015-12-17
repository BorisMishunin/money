# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentstype',
            name='desc',
            field=models.TextField(default=' django.utils.timezone.now()', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentstype',
            name='icon',
            field=models.ImageField(upload_to='foto', default='', verbose_name='Иконка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 14, 17, 48, 797383), verbose_name='Дата'),
        ),
    ]
