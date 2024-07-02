
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class FormularioImagen(UserChangeForm):
    imagen = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['imagen']