from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name=models.CharField(max_length=1000)

class Message(models.Model):
    value=models.CharField(max_length=5000000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=1000)
    room=models.CharField(max_length=1000)

# class profile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     pic=models.ImageField(upload_to="img",blank=True,null=True)

#     def __str__(self) :
#         return self.name

# class Friend(models.Model):
#     pass