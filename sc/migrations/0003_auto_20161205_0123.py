# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-05 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0002_citizen_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='who',
            field=models.IntegerField(verbose_name='From (1-Hillary, 2-Trump, 3-Jill, 4-Gary)'),
        ),
    ]
