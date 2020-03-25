from django.contrib import admin
from django.conf.urls import url
from app1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/$', views.help, name='help'),
    url(r'^users/$', views.users, name='users'),
]
