from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ("username","email","password")