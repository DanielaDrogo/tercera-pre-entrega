from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('perfil/ver', views.ver_perfil, name='ver_perfil'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
