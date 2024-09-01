from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_publicacion, name='agregar_publicacion'),
    path('editar/<pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('lista/', views.lista_publicaciones, name='lista_publicaciones'),
]

path('detalles/<pk>/', views.detalles_publicacion, name='detalles_publicacion'),