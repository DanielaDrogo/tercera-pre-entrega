from django import forms
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import Blog
from .models import Blog


class BlogForm(forms.ModelForm):
    
    
    class Meta:
        model = Blog
        fields = ['imagen', 'subtitulo', 'titulo', 'cuerpo']