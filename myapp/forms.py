# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Maquina

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['tipo', 'marca', 'modelo', 'no_serie', 'observaciones']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
