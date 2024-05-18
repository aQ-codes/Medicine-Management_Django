#your model forms goes here
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User  #default django user  model that we see in admin panel

from .models import Medicine

class MedicineForm(ModelForm):
    class Meta:
        model =  Medicine
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),  
        }
      
      
class CreateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
