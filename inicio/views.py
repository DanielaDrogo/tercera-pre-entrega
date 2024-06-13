from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
from django.http import HttpResponse
from django.template import Template, context, loader

from inicio.models import planta
from inicio.forms import CrearPlantaFormulario

import random

def inicio(request):
    return render(request, 'inicio/index.html')


def template1(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi template 1</h1> -- fecha: {fecha} -- bienvenido {nombre} {apellido}')


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
            return redirect('inicio')
    
    formulario = CrearPlantaFormulario()
    return render(request, 'inicio/crear_planta2.html', {'formulario': formulario})
    
    
    
def plantas(request):
    plantas = planta.objects.all()
    return render(request, 'inicio/plantas.html', {'plantas': plantas})   
    
    
    
    