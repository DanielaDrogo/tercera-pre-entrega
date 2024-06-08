from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola bienvenidos a mi INICIO :D')