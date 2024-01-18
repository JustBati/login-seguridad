from django import forms
from .models import Maquina

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['tipo', 'marca', 'modelo', 'no_serie', 'observaciones']