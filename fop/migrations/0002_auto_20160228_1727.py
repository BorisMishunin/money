# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxe_payments',
            name='date_to',
            field=models.DateField(default=datetime.datetime(2016, 2, 28, 17, 27, 25, 16616, tzinfo=utc), verbose_name='Период по'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='taxe_payments',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='taxe_payments',
            name='date_from',
            field=models.DateField(verbose_name='Период с'),
        ),
    ]
