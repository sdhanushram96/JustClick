from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Device ID',help_text='Provide Device ID *Required*|Check backside of your Product|')
    first_name = forms.CharField(max_length=200, required=True, help_text='Required for Delivery', label='Address')
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    last_name = forms.CharField(max_length=200, help_text='Required User Name',label='Name')

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email','first_name', 'password1', 'password2', )
