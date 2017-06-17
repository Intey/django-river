# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0009_auto_20170124_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceedingmeta',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', verbose_name='Groups'),
        ),
        migrations.AlterField(
            model_name='proceedingmeta',
            name='parents',
            field=models.ManyToManyField(db_index=True, related_name='children', to='river.ProceedingMeta', verbose_name='parents'),
        ),
    ]