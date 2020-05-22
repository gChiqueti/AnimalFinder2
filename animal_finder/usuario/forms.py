from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    telefone = forms.IntegerField(max_value=99999999999)

    class Meta:
    	model = User
    	fields = ["username", "telefone", "email", "password1", "password2"]
