from django import forms
from .models import Tarefa

from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class CadastrarTarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "data_entrega"]
        widgets= {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'titulo'
            }),
            'data_entrega': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'data_entrega'
            }),
        }
class AtulizarTarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        widgets= {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'titulo'
            }),
            'data_entrega': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'data_entrega'
            }),
        }