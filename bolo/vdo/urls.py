from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vdo_home),
    path('vdo-home', views.vdo_home),
    path('room', views.room),
]