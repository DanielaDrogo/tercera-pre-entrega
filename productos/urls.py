from django.urls import path
from . import views

urlpatterns = [
    path("macetas/", views.Macetas.as_view(), name='macetas'),
    path("macetas/crear/", views.CrearMaceta.as_view(), name='crear_maceta'),
    path("macetas/<int:pk>/", views.VerMaceta.as_view(), name='ver_maceta'), 
    path("macetas/editar/<int:pk>/", views.EditarMaceta.as_view(), name='editar_maceta'), 
    path("macetas/eliminar/<int:pk>/", views.EliminarMaceta.as_view(), name='eliminar_maceta'),

]



