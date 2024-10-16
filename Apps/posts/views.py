from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, User, Comentarios
from django.contrib.auth.decorators import login_required
from .models import Posts, Comentarios  # Asegúrate de que tus modelos estén correctamente importados
from django import forms
from django.views.generic import CreateView, UpdateView, DeleteView # Importa CreateView
from django.urls import reverse_lazy
from .form import RegistroForm, ComentarioForm
from .form import LoginForm

def posts(request):
    ctx = {}
    noticias = Posts.objects.all()
    ctx["noticias"] = noticias
    return render(request, "posts/posts.html", ctx)

@login_required  # Asegúrate de que solo usuarios autenticados puedan comentar
def post_id(request, id):
    post = get_object_or_404(Posts, id=id)
    comentarios = Comentarios.objects.filter(post=post)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  # Asocia el comentario al post
            comentario.autor = request.user  # Asocia el comentario al usuario autenticado
            comentario.save()
            return redirect('postindividual', id=post.id)  # Redirige después de guardar
    else:
        form = ComentarioForm()

    ctx = {
        'post': post,
        'comentarios': comentarios,
        'form': form,
    }

    return render(request, "posts/postindividual.html", ctx)

def about_us(request):
    return render(request, "posts/quienessomos.html")

def registro(request):
    return render(request, "usuarios/registro.html")

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Lógica de autenticación aquí
            pass
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})

def contactanos_view(request):
    return render(request, 'posts/contactanos.html')


from .form import PostForm

@login_required  # Asegúrate de que solo los usuarios autenticados puedan agregar posts
def nuevo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # request.FILES para manejar imágenes
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Asigna el autor como el usuario que está logueado
            post.save()
            return redirect('noticias')  # Redirige a la lista de noticias después de agregar
    else:
        form = PostForm()
    
    return render(request, 'posts/nuevo_post.html', {'form': form})


@login_required 
def eliminar_post(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('noticias')  # Redirige a la lista de noticias después de eliminar
    return render(request, "posts/postindividual.html", {'post': post})

