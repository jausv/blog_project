Paso 1: Crear un proyecto de Django
Abre una terminal o línea de comandos y ejecuta el siguiente comando:

django-admin startproject blog_project

Esto creará un nuevo directorio llamado blog_project con la estructura básica de un proyecto de Django.

Paso 2: Crear una nueva aplicación dentro del proyecto
Navega al directorio blog_project y ejecuta el siguiente comando:

python manage.py startapp blog

Esto creará un nuevo directorio llamado blog dentro de blog_project, que contendrá la lógica específica de tu aplicación de blog.

Paso 3: Configurar el modelo de datos
En el archivo blog/models.py, define el modelo Post con los campos especificados en el enunciado del proyecto:

from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    
Guardar los cambios en el archivo.

Paso 4: Crear la base de datos y aplicar las migraciones
Ejecuta los siguientes comandos en la terminal:

python manage.py makemigrations
python manage.py migrate

Esto creará la base de datos y aplicará las migraciones necesarias para el modelo Post.

Paso 5: Crear formularios basados en modelos
En el archivo blog/forms.py, crea un nuevo formulario basado en el modelo Post:

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor')
        
Este formulario utilizará los campos del modelo Post para crear un formulario de entrada.

Paso 6: Crear vistas para agregar y editar publicaciones
En el archivo blog/views.py, crea dos nuevas vistas:

from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def agregar_publicacion(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PostForm()
    return render(request, 'blog/agregar_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_publicacion.html', {'form': form})
    
La vista agregar_publicacion maneja la creación de nuevas publicaciones.
La vista editar_publicacion maneja la edición de publicaciones existentes.

Paso 7: Crear templates para las vistas
Crea dos nuevos archivos HTML en el directorio blog/templates/blog/:

agregar_publicacion.html
editar_publicacion.html

En estos archivos, crea un formulario que utilice el formulario PostForm creado anteriormente.

Paso 8: Crear la vista de lista de publicaciones
En el archivo blog/views.py, agrega una nueva vista:

def lista_publicaciones(request):
    publicaciones = Post.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})
Esta vista recupera todas las publicaciones de la base de datos y las pasa a un template llamado lista_publicaciones.html.

Paso 9: Crear el template de lista de publicaciones
Crea un nuevo archivo HTML en el directorio blog/templates/blog/:

lista_publicaciones.html

En este archivo, crea una lista que muestre las publicaciones:

<h1>Lista de publicaciones</h1>
<ul>
    {% for publicacion in publicaciones %}
        <li>
            <h2>{{ publicacion.titulo }}</h2>
            <p>{{ publicacion.contenido }}</p>
            <p>Fecha de publicación: {{ publicacion.fecha_publicacion }}</p>
            <p>Categoría: {{ publicacion.categoria }}</p>
            <p>Autor: {{ publicacion.autor }}</p>
        </li>
    {% endfor %}
</ul>

Este template utiliza una plantilla de Django para mostrar las publicaciones.

Paso 10: Agregar URLs para las vistas
En el archivo blog/urls.py, agrega las siguientes líneas:

from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_publicacion, name='agregar_publicacion'),
    path('editar/<pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('lista/', views.lista_publicaciones, name='lista_publicaciones'),
]
Estas líneas agregan URLs para las vistas agregar_publicacion, editar_publicacion y lista_publicaciones.

Paso 11: Agregar búsqueda y filtración a la lista de publicaciones
En el archivo blog/views.py, modifica la vista lista_publicaciones para agregar búsqueda y filtración:

def lista_publicaciones(request):
    publicaciones = Post.objects.all()
    query = request.GET.get('q')
    if query:
        publicaciones = publicaciones.filter(titulo__icontains=query) | publicaciones.filter(contenido__icontains=query)
    categoria = request.GET.get('categoria')
    if categoria:
        publicaciones = publicaciones.filter(categoria=categoria)
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})
    
Esta vista ahora busca publicaciones por título o contenido, y también filtra por categoría.

Paso 12: Agregar formularios de búsqueda y filtración al template
En el archivo blog/templates/blog/lista_publicaciones.html, agrega los siguientes formularios:

<form action="" method="get">
    <input type="text" name="q" placeholder="Buscar...">
    <button type="submit">Buscar</button>
</form>

<form action="" method="get">
    <select name="categoria">
        <option value="">Todas las categorías</option>
        {% for categoria in publicaciones.values_list('categoria', flat=True).distinct %}
            <option value="{{ categoria }}">{{ categoria }}</option>
        {% endfor %}
    </select>
    <button type="submit">Filtrar</button>
</form>

Estos formularios permiten al usuario buscar y filtrar publicaciones.

Paso 13: Crear la vista de detalles de la publicación
En el archivo blog/views.py, agrega una nueva vista:

def detalles_publicacion(request, pk):
    publicacion = Post.objects.get(pk=pk)
    return render(request, 'blog/detalles_publicacion.html', {'publicacion': publicacion})
    
Esta vista recupera una publicación específica por su ID y la pasa a un template llamado detalles_publicacion.html.

Paso 14: Crear el template de detalles de la publicación
Crea un nuevo archivo HTML en el directorio blog/templates/blog/:

detalles_publicacion.html

En este archivo, muestra los detalles de la publicación:

<h1>{{ publicacion.titulo }}</h1>
<p>{{ publicacion.contenido }}</p>
<p>Fecha de publicación: {{ publicacion.fecha_publicacion }}</p>
<p>Categoría: {{ publicacion.categoria }}</p>
<p>Autor: {{ publicacion.autor }}</p>
Este template muestra los detalles de la publicación.

Paso 15: Agregar URL para la vista de detalles
En el archivo blog/urls.py, agrega la siguiente línea:

path('detalles/<pk>/', views.detalles_publicacion, name='detalles_publicacion'),

Esta línea agrega una URL para la vista de detalles de la publicación.

El blog básico en Django está listo para ser probado. Pasos para probarlo:
1. Iniciar el servidor de Django
Abre una terminal y navega al directorio del proyecto.
Ejecuta el comando python manage.py runserver para iniciar el servidor de Django.
2. Abrir el navegador
Abre un navegador web y escribe la URL http://localhost:8000/ para acceder al blog.
3. Probar las funcionalidades
Prueba agregar una nueva publicación.
Prueba editar una publicación existente.
Prueba buscar publicaciones por título o contenido.
Prueba filtrar publicaciones por categoría.
Prueba ver los detalles de una publicación específica.

