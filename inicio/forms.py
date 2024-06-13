from django import forms 

class CrearPlantaFormulario(forms.Form):
    tipo = forms.CharField(max_length=30)
    especie = forms.CharField(max_length=30)



