from django.contrib import admin

# Register your models here.
from .models import Citizen
from .models import Tweet

admin.site.register(Citizen)


class TweetAdmin(admin.ModelAdmin):
    fields = ['content', 'type', 'who']
    list_display = ('id', 'content', 'type', 'who')
    search_fields = ['content']


admin.site.register(Tweet, TweetAdmin)