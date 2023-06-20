from django import forms
from .models import Pessoa

class formularioCadastro(forms.Form):
    nome = forms.CharField(max_length=10)
    email = forms.EmailField()

class formularioCadastroModel(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'email'
        )