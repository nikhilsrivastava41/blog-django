from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('postcomment', views.postcomment, name='postcomment'),
    path('', views.home, name='home'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]
