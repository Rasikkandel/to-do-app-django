form django import forms 
from django.forms import ModelForm 
from . models import * 

class tasks(forms.ModelForm) : 
    class meta : 
        model = taskss 
        field = '__all__'
