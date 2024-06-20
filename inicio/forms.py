from django import forms 

class PlantaFormularioBase(forms.Form):
    tipo = forms.CharField(max_length=30)
    especie = forms.CharField(max_length=30)


class CrearPlantaFormulario(PlantaFormularioBase):
    ...
        
class EditarPlantaFormulario(PlantaFormularioBase):
    ...
    
class BuscarPlanta(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)

    

    


