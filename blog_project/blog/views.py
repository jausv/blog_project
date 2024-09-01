from django.shortcuts import render

# Create your views here.
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

def lista_publicaciones(request):
    publicaciones = Post.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})


def agregar_publicacion(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            pass
    return render(request, 'blog/agregar_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion = Post.objects.get(pk=pk)
    form = PostForm(instance=publicacion)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=publicacion)
        if form.is_valid():
            # Procesar el formulario
            pass
    return render(request, 'blog/editar_publicacion.html', {'form': form})

def lista_publicaciones(request):
    publicaciones = Post.objects.all()
    query = request.GET.get('q')
    if query:
        publicaciones = publicaciones.filter(titulo__icontains=query) | publicaciones.filter(contenido__icontains=query)
    categoria = request.GET.get('categoria')
    if categoria:
        publicaciones = publicaciones.filter(categoria=categoria)
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalles_publicacion(request, pk):
    publicacion = Post.objects.get(pk=pk)
    return render(request, 'blog/detalles_publicacion.html', {'publicacion': publicacion})
