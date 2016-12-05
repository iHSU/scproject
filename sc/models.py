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

    def __str__(self):
        return self.name

    def format_time(self):
        # return self.create_time.strftime("%b-%d-%y %H:%M:%S")
        return self.create_time.strftime("%d/%m/%Y")


class Tweet(models.Model):
    content = models.CharField(max_length=200, verbose_name='Tweet Content')
    type = models.IntegerField(verbose_name='Type (1-Original, 2-Fake)') # 1, original 2, fake
    who = models.IntegerField(verbose_name='From (1-Hillary, 2-Trump, 3-Jill, 4-Gary)') # 1 Hillary 2 Trump
    weight = models.IntegerField(default=0, verbose_name='Weight')

    def __str__(self):
        return self.content.encode('utf-8').strip()


class Result(models.Model):
    citizen = models.ForeignKey(Citizen)
    tweet = models.ForeignKey(Tweet)
    attitude = models.IntegerField() # 1 like, -1 dislike
    create_time = models.DateTimeField(auto_now=True, verbose_name='Create Time')

    def format_time(self):
        # return self.create_time.strftime("%b-%d-%y %H:%M:%S")
        return self.create_time.strftime("%d/%m/%Y")
