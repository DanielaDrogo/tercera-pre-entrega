from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse
from django.template import Template, context, loader

import random

def inicio(request):
    return HttpResponse('Hola bienvenidos a mi INICIO :D')


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
    
    