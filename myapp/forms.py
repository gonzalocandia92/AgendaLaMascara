from django.forms import ModelForm, DateInput
from django import forms
from datetime import datetime
from .models import *



class EventForm(ModelForm):
    start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', "class": "form-control"}), initial=datetime.now())
    end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', "class": "form-control"}), initial=datetime.now())
        
    class Meta:
        model = Events
        fields = ["name", "start", "end"]
        
        
       