from django.urls import re_path

from . import views

app_name = 'test_app'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.detail, name='detail'),
    re_path(r'^([0-9]+)/answer/$', views.answer, name='answer')
]
