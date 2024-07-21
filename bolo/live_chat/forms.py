from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class ChatMessageForm(ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":1,"id":"iid3","placeholder":"Type Message Here..."}))
    class Meta:
        model=ChatMessage
        fields=["body",]
