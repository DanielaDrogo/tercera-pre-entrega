from django.urls import path
from blog import views 


urlpatterns = [
    # path('blog/', views.blog_hola, name='lista_blogs'),
    path('', views.lista_blogs, name='lista_blogs'),
    path('blog/<int:blog_id>/', views.BlogFecha, name='lista_blogs'),
      
]
