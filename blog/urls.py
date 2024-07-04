from django.urls import path
from blog import views 


# urlpatterns = [
#     # path('blog/', views.blog_hola, name='lista_blogs'),
#     path('', views.lista_blogs, name='lista_blogs'),
#     path('blog/<int:blog_id>/', views.BlogFecha, name='lista_blogs'),
      
# ]

urlpatterns = [
    path('', views.BlogListView.as_view(), name='lista_blogs'),
    path('crear/', views.BlogCreateView.as_view(), name='blog_crear'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detalle'),
    path('<int:pk>/editar/', views.BlogUpdateView.as_view(), name='blog_editar'),
    path('<int:pk>/eliminar/', views.BlogDeleteView.as_view(), name='blog_eliminar'),
]