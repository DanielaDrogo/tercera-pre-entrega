from django.urls import path
from inicio import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('template1/<str:nombre>/<str:apellido>', views.template1),
    path('template2/<str:nombre>/<str:apellido>', views.template2, name="template2"),
    path('probando', views.probando, name="probando"),
    path('planta/crear/<str:tipo>/<str:especie>/', views.crear_planta, name="crear_planta"),
]


