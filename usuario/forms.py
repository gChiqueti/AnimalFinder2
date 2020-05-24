from .models import Dono
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "As senhas não conferem",
    }


    email = forms.EmailField(help_text='Required. Add a valid email address',
                            label='email',
                            widget=forms.EmailInput(
                                     attrs={'placeholder': 'Digite seu e-email',
                                            'class': 'input'}))
    nome = forms.CharField(label='password',
                           widget=forms.TextInput(
                                attrs={'placeholder': 'Nome completo',
                                       'class': 'input'}))
    telefone = forms.IntegerField(label='telefone',
                                  widget=forms.NumberInput(
                                    attrs={'placeholder': 'Telefone',
                                           'class': 'input'}))

    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput(
                                        attrs={'placeholder': 'Senha',
                                               'class': 'input'}))
    password2 = forms.CharField(label='password',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Confirme a senha',
                                           'class': 'input'}))

    class Meta:
        model = Dono
        fields = ("email", "nome", "telefone", "password1", "password2")


    # verificar os inputs (se as senhas batem)
    def clean(self):
            cleaned_data = super(RegistrationForm, self).clean()
            password = cleaned_data.get("password1")
            confirm_password = cleaned_data.get("password2")

            if password != confirm_password:
                raise forms.ValidationError("As senhas nao conferem")



class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(
                   label='password',
                   widget=forms.PasswordInput(
                            attrs={'placeholder': 'Digite sua senha',
                                   'class': 'input'}))
    email = forms.EmailField(
                       label='email',
                       widget=forms.EmailInput(
                                attrs={'placeholder': 'Digite seu e-email',
                                       'class': 'input'}))
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
