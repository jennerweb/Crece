# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-20 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='correo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='edad',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='experiencia_anos',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombres',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='profesion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Profesiones'),
        ),
    ]
