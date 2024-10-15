from django.shortcuts import render, redirect
from .models import Posts, User, Comentarios
from django import forms

# Create your views here.

# vista basada en funciones
def posts(request):
    ctx = {}  # contextos/ diccionarios CONSULTAR
    noticias = Posts.objects.all()  # select * from Posts
    ctx["noticias"] = noticias
    # print(noticias)
    return render(request, "posts/posts.html", ctx)

def post_id(request, id):
    ctx = {}
    noticia = Posts.objects.get(id=id)
    comentarios = Comentarios.objects.filter(post=noticia)
    ctx["noticia"] = noticia
    ctx["comentarios"] = comentarios
    return render(request, "posts/detalle.html", ctx)

def about_us(request):
    return render(request, "posts/quienessomos.html")

def registro(request):
    return render(request,"usuarios/registro.html")

# vistas badas en clases

from .form import RegistroForm
from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"

from django.shortcuts import render

from .form import LoginForm  # Asegúrate de que esto esté correcto
  # Asegúrate de importar el nuevo formulario

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Aquí va la lógica de autenticación
            pass
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})




def contactanos_view(request):
    return render(request, 'posts/contactanos.html')


