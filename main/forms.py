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
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do animal', 'class': 'input'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Idade do animal (anos)', 'class': 'input'}),
            'cidade_desaparecimento': forms.TextInput(attrs={'placeholder': 'Cidade do desaparecimento', 'class': 'input'}),
            'estado_desaparecimento': forms.TextInput(attrs={'placeholder': 'Estado do desaparecimento', 'class': 'input'}),
            'informacoes_extras': forms.TextInput(attrs={'placeholder': 'Informações extras', 'class': 'input'}),
        }

class ContatoForm(forms.ModelForm):
    nome = forms.CharField(label='password',
                           widget=forms.TextInput(
                                attrs={'placeholder': 'Nome completo',
                                       'class': 'input'}))
    telefone = forms.IntegerField(label='telefone',
                                  widget=forms.NumberInput(
                                    attrs={'placeholder': 'Telefone para contato',
                                           'class': 'input'}))

    class Meta:
        model = Contato
        fields = ['nome',
                  'telefone'
                   ]
