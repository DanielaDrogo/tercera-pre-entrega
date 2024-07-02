from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, context, loader

from inicio.models import planta
from inicio.forms import CrearPlantaFormulario, BuscarPlanta, EditarPlantaFormulario

import random

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')


# def template1(request, nombre, apellido):
#     fecha = datetime.now()
#     return HttpResponse(f'<h1>Mi template 1</h1> -- fecha: {fecha} -- bienvenido {nombre} {apellido}')


def template2(request, nombre, apellido):
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido
    }
    return render(request, 'template2.html', datos)


def probando(request):
    
    lista = list(range(100))
    numeros = random.choices(lista, k=20)
    print(numeros)
    
    return render(request, 'probando_if_for.html', {'numeros': numeros})


    
def crear_planta(request, tipo, especie):
    mi_planta = planta(tipo=tipo, especie=especie)
    mi_planta.save()
    return render(request, 'plantas_template/creacion.html', {"planta": mi_planta})
    
    
    
def crear_planta2(request):
    print('valor de la request: ', request)
    print('valor de GET: ', request.GET)
    print('valor de POST: ', request.POST)
    
    if request.method == 'POST':
        formulario = CrearPlantaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            mi_planta = planta(tipo=request.POST.get('tipo'), especie=request.POST.get('especie'))
            mi_planta.save()
            return redirect('plantas')
    
    formulario = CrearPlantaFormulario()
    return render(request, 'inicio/crear_planta2.html', {'formulario': formulario})
    
    
    
def plantas(request):
    
    formulario = BuscarPlanta(request.GET)
    if formulario.is_valid():
        tipo = formulario.cleaned_data['tipo']
        plantas = planta.objects.filter(tipo__icontains=tipo)
    
    # plantas = planta.objects.all()
    return render(request, 'inicio/plantas.html', {'plantas': plantas, 'formulario': formulario})   
    
  
@login_required
def eliminar_planta(request, id):
    mi_planta = planta.objects.get(id=id)
    mi_planta.delete()
    
    return redirect('plantas')


@login_required
def editar_planta(request, id):
    mi_planta = planta.objects.get(id=id)
    
    formulario = EditarPlantaFormulario(initial={'tipo': mi_planta.tipo, 'especie': mi_planta.especie})
    
    if request.method == 'POST':
        formulario = EditarPlantaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            mi_planta.tipo = info['tipo']
            mi_planta.especie = info['especie']
            mi_planta.save()
            return redirect('plantas')
    
    return render(request, 'inicio/editar_planta.html', {'formulario': formulario, 'planta': mi_planta})


def ver_planta(request, id):
    mi_planta = planta.objects.get(id=id)
    return render(request, 'inicio/ver_planta.html', {'mi_planta': mi_planta})






  
    
    
    