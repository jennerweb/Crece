# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-20 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20170520_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='experiencia_horas',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
    ]
