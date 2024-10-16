from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Comentarios  
from django.contrib.auth.decorators import login_required
from .form import RegistroForm, ComentarioForm, PostForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .form import LoginForm  


def posts(request):
    ctx = {}
    noticias = Posts.objects.all()
    ctx["noticias"] = noticias
    return render(request, "posts/posts.html", ctx)

def post_id(request, id):
    post = get_object_or_404(Posts, id=id)
    comentarios = Comentarios.objects.filter(post=post)
    form = ComentarioForm()  

    return render(request, 'posts/postindividual.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
    })

@login_required
def agregar_comentario(request, post_id):
    post = get_object_or_404(Posts, id=post_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user 
            comentario.save()
            return redirect('post_individual', id=post.id)  
    else:
        form = ComentarioForm()

    return render(request, 'posts/postindividual.html', {
        'post': post,
        'form': form,
    })

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
            
            pass
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})

def contactanos_view(request):
    return render(request, 'posts/contactanos.html')

@login_required  
def nuevo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  
            post.save()
            return redirect('noticias')  
    else:
        form = PostForm()
    
    return render(request, 'posts/nuevo_post.html', {'form': form})

@login_required 
def eliminar_post(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('noticias')  
    return render(request, "posts/postindividual.html", {'post': post})

