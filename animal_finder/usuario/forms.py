from .models import Dono
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Dono
        fields = ("email", "nome", "telefone", "password1", "password2")


class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    class Meta:
        model = Dono
        fields = ['email', 'password']

    def clean(self):
        if not self.is_valid():
            return
        email    = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")
