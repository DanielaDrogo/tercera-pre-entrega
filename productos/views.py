from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Maceta
from django.urls import reverse_lazy

# Create your views here.


# def macetas(request):
#     return HttpResponse('vista de macetas')

class Macetas(ListView):
    model = Maceta
    template_name = 'macetas/lista_de_macetas.html'
    context_object_name = 'macetas'


class CrearMaceta(CreateView):
    model = Maceta
    template_name = 'macetas/crear_maceta.html'
    success_url = reverse_lazy ('macetas')
    fields = ['tamanio', 'material', 'precio']


class EditarMaceta(UpdateView):
    model = Maceta
    template_name = 'macetas/editar_maceta.html'
    success_url = reverse_lazy ('macetas')
    fields = ['tamanio', 'material', 'precio']
    


class VerMaceta(DetailView):
    model = Maceta
    template_name = 'macetas/ver_maceta.html'
    

class EliminarMaceta(DeleteView):
        model = Maceta
        template_name = 'macetas/eliminar_maceta.html'
        success_url = reverse_lazy ('macetas')



