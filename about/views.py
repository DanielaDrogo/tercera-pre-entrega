from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def hola(request):
#     return HttpResponse('hola')

def AboutMe(request):
    return render(request, 'aboutme/sobre_mi.html')