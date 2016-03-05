# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20151227_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstranscript',
            name='payment',
            field=models.ForeignKey(related_name='payments_transcript', to='web.Payments', verbose_name='Платеж'),
        ),
    ]
