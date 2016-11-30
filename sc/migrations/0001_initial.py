# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age_level', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('occupation', models.CharField(max_length=150)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attitude', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('citizen', models.ForeignKey(to='sc.Citizen')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200, verbose_name='Tweet Content')),
                ('type', models.IntegerField(verbose_name='Type (1-Original, 2-Fake)')),
                ('who', models.IntegerField(verbose_name='From (1-Hillary, 2-Trump)')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='tweet',
            field=models.ForeignKey(to='sc.Tweet'),
        ),
    ]
