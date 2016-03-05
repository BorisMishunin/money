# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0002_auto_20151218_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='icon',
            field=models.ImageField(verbose_name='Аватар', upload_to='users_foto'),
        ),
    ]
