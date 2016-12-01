from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start$', views.start, name='start'),
    url(r'^result$', views.result, name='result'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^statistics', views.total_result, name='total_result'),
]
