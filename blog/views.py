from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    model = Blog
    template_name = 'miblog/lista_blog.html'
    context_object_name = 'blogs'
    
class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'miblog/blog_form.html'
    success_url = reverse_lazy('lista_blogs')
    

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'miblog/blog_form.html'
    success_url = reverse_lazy('lista_blogs')
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'miblog/blog_detalle.html'
    
class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'miblog/blog_confirm_delete.html'
    success_url = reverse_lazy('lista_blogs')









