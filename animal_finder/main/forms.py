from django import forms
from .models import Animal, Contato

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['foto',
                  'nome',
                  'idade',
                  'cidade_desaparecimento',
                  'estado_desaparecimento',
                  'status',
                  'informacoes_extras']

        # estilo
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do animal', 'class': 'input'}),
            'idade': forms.TextInput(attrs={'placeholder': 'Digite a idade do animal', 'class': 'input'}),
            'cidade_desaparecimento': forms.TextInput(attrs={'placeholder': 'Digite a cidade do desaparecimento', 'class': 'input'}),
            'estado_desaparecimento': forms.TextInput(attrs={'placeholder': 'Digite o estado do desaparecimento', 'class': 'input'}),
            'informacoes_extras': forms.TextInput(attrs={'placeholder': 'Digite alguma informação extra', 'class': 'input'}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome',
                  'telefone'
                   ]
