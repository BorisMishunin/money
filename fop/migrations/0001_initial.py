# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Имя', max_length=150)),
            ],
            options={
                'verbose_name': 'ФОП',
                'verbose_name_plural': 'ФОП',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата', auto_now=True)),
                ('summ_gross', models.FloatField(verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.CreateModel(
            name='Taxe_Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата', auto_now=True)),
                ('date_from', models.DateField(verbose_name='Период по', auto_now=True)),
                ('summ', models.FloatField(verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Налоговый платеж',
                'verbose_name_plural': 'Налоговые платежи',
            },
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Имя налога', max_length=150)),
                ('count_method', models.IntegerField(verbose_name='Метод расчета', default=0, choices=[(0, 'Фиксированная сумма'), (1, 'Процентом')])),
                ('summ', models.FloatField(verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.AddField(
            model_name='taxe_payments',
            name='taxe',
            field=models.ForeignKey(to='fop.Taxes', verbose_name='Налог'),
        ),
    ]
