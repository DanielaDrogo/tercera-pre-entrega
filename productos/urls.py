from django.urls import path
from . import views

urlpatterns = [
    path("macetas/", views.Macetas.as_view(), name='macetas'),
    path("macetas/crear/", views.CrearMaceta.as_view(), name='crear_maceta'),

]



