# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('icon', models.ImageField(verbose_name='Фото', upload_to='users_foto')),
                ('see_itself_notes', models.BooleanField(verbose_name='Отображать только записи пользователя')),
                ('user', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вид платежа',
                'verbose_name_plural': 'Виды платежа',
            },
        ),
    ]
