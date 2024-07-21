from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    passwd=models.CharField(max_length=100,blank=True,null=True)
    # pic=models.ImageField(upload_to="img",blank=True,null=True)
    friends=models.ManyToManyField('Friend',related_name='my_friends',blank=True,null=True)
    # date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name

class Friend(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.profile.name

class ChatMessage(models.Model):
    body=models.TextField()
    msg_sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='msg_sender')
    msg_reciever=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='msg_reciever')
    seen=models.BooleanField(default=False)

    def __str__(self):
        return self.body