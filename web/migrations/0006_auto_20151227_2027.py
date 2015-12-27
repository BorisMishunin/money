# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20151222_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(verbose_name='Дата', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payments',
            name='month',
            field=models.DateTimeField(verbose_name='Месяц', default=django.utils.timezone.now),
        ),
    ]
