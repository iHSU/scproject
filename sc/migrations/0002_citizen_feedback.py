# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='feedback',
            field=models.TextField(verbose_name='Feedback', blank=True),
        ),
    ]
