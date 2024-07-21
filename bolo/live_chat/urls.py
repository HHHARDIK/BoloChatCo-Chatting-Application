from . import views
from django.urls import path,include

urlpatterns = [
    path('/about',views.about,name="about"),
    path('',views.about),
    path('/forgot',views.forgot,name="/forgot"),
    path('/ver_em',views.ver_em,name="ver_em"),
    path('/change_pass',views.change_pass,name="change_pass"),
    path('/reset',views.reset,name="reset"),
    path('/account',views.index,name="index"),
    path('/login/',views.login,name="/login"),
    path('/login/handle_signup',views.handle_signup,name="handle_signup"),
    path('/friend/<str:pk>',views.detail,name="detail"),
    path("sent_msg/<str:pk>",views.sentMessages,name="sent_msg"),
    path("rec_msg/<str:pk>",views.recievedMessages,name="rec_msg"),
    path('notification',views.chatNotification,name="notification"),
    path('/logout',views.logout,name="/logout"),
]