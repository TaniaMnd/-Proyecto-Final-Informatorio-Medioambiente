from django.shortcuts import render, redirect
from .models import Posts, User, Comentarios
from django import forms


def posts(request):
    ctx = {}  
    noticias = Posts.objects.all()  
    ctx["noticias"] = noticias

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


from .form import RegistroForm
from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"

from django.shortcuts import render

from .form import LoginForm  
  

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
        
            pass
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})




def contactanos_view(request):
    return render(request, 'posts/contactanos.html')


