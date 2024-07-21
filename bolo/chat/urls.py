from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.chat_home),
    path('chat', views.chat_home),
    path('checkroom', views.checkroom),
    path('<str:room>/',views.chat_room,name='room'),
    path('send',views.send,name='send'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
]
