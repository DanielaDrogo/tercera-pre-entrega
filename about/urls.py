from django.urls import path
from about import views 
from about.views import AboutMe


urlpatterns = [
    path('', views.AboutMe, name='about_me'),
      
]