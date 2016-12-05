from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start$', views.start, name='start'),
    url(r'^result$', views.result, name='result'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^total$', views.total_result, name='total_result'),
    url(r'^manage$', views.manage, name='manage'),
    url(r'users$', views.users, name='users'),
    url(r'specific', views.specific_user_result, name='specific_user_result'),
]
