from django.contrib import admin

# Register your models here.
from .models import Citizen
from .models import Tweet
from .models import Result


class TweetAdmin(admin.ModelAdmin):
    fields = ['content', 'type', 'who']
    list_display = ('id', 'content', 'type', 'who', 'weight')
    search_fields = ['content']


class CitizenAdmin(admin.ModelAdmin):
    fields = ['name', 'age_level', 'gender', 'occupation', 'feedback', 'create_time']
    list_display = ('id','name', 'age_level', 'gender', 'occupation', 'feedback', 'create_time')


class ResultAdmin(admin.ModelAdmin):
    fields = ['citizen', 'tweet', 'attitude', 'create_time']
    list_display = ('citizen', 'tweet', 'attitude', 'create_time')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Citizen, CitizenAdmin)
admin.site.register(Result, ResultAdmin)