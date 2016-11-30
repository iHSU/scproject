from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Citizen(models.Model):
    name = models.CharField(max_length=100)
    age_level = models.IntegerField()
    gender = models.IntegerField()
    occupation = models.CharField(max_length=150)
    feedback = models.TextField(verbose_name='Feedback', blank=True)
    create_time = models.DateTimeField(auto_now=True, verbose_name='Create Time')


class Tweet(models.Model):
    content = models.CharField(max_length=200, verbose_name='Tweet Content')
    type = models.IntegerField(verbose_name='Type (1-Original, 2-Fake)') # 1, original 2, fake
    who = models.IntegerField(verbose_name='From (1-Hillary, 2-Trump)') # 1 Hillary 2 Trump


class Result(models.Model):
    citizen = models.ForeignKey(Citizen)
    tweet = models.ForeignKey(Tweet)
    attitude = models.IntegerField() # 1 like, -1 dislike
    create_time = models.DateTimeField(auto_now=True, verbose_name='Create Time')
