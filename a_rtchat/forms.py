from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': '🙂 Type a message', 'class': 'form-control input', 'maxlength' : '300', 'autofocus': True }),
        }
    
    