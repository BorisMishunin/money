# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=150)),
                ('cost', models.IntegerField(null=True, verbose_name='Стоимость', blank=True)),
            ],
            options={
                'verbose_name': 'Товары или услуги',
                'verbose_name_plural': 'Товар или услуга',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField(verbose_name='Дата', default=datetime.datetime(2015, 12, 16, 22, 11, 45, 397261))),
                ('month', models.DateTimeField(verbose_name='Месяц')),
                ('total', models.IntegerField(verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.CreateModel(
            name='PaymentsTranscript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('summ', models.IntegerField(verbose_name='Сумма')),
                ('payment', models.ForeignKey(verbose_name='Платеж', to='web.Payments')),
                ('payment_good', models.ForeignKey(verbose_name='Товар или услуга', to='web.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=150)),
            ],
            options={
                'verbose_name': 'Вид платежа',
                'verbose_name_plural': 'Виды платежа',
            },
        ),
        migrations.AddField(
            model_name='payments',
            name='payment',
            field=models.ForeignKey(verbose_name='Вид платежа', to='web.PaymentsType'),
        ),
    ]
