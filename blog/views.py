from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.http import HttpResponse
from datetime import datetime

from blog.forms import FormularioImagen

# Create your views here.

def blog_hola(request):
    return HttpResponse(request)


def lista_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'miblog/lista_blog.html', {'blogs': blogs})


def BlogFecha(request, blog_id):
    blogs = Blog
    fecha = datetime.now(Blog, pk=blog_id)
    datos = {
        'fecha': fecha,
    }
    return render(request, 'miblog/lista_blog.html', datos, {'blogs': blogs})



def BlogImagen(request):
    
    datosextra = request.user.datosextra
    formulario = FormularioImagen(initial={'imagen': datosextra.imagen}, instance=request.user)
    
    if request.method == "POST":
        formulario = FormularioImagen(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            datosextra.imagen = formulario.cleaned_data.get('imagen')
            datosextra.save()
            
            formulario.save()
            return redirect('lista_blog')
    
    return render(request, 'blog/lista_blog.html', {'formulario': formulario})



# def BlogFecha(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'miblog/lista_blog.html', {'blog': blog})




