from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria, Comentario
from django.core.paginator import Paginator
from .form import ComentarioForm, RegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test


def posts(request):
    categorias = Categoria.objects.all()  
    selected_categoria = request.GET.get('categoria')  

    # Filtrar los posts
    if selected_categoria:
        posts = Post.objects.filter(categoria__nombre=selected_categoria).order_by('-publicado')
    else:
        posts = Post.objects.all().order_by('-publicado')  

    # Paginación
    paginator = Paginator(posts, 9)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'index.html', {'posts': page_obj, 'categorias': categorias})


def is_staff(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_staff) 
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts') 


#vista para quienes somos
def quienessomos(request):
    return render(request, 'quienessomos.html')

#vista para sobreelproyecto
def sobrelproyecto(request):
    return render(request, 'sobrelproyecto.html')


# VISTA POST ESPECIFICOS (NOTICIAS)
def postindividual(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    comentarios_list = Comentario.objects.filter(post=post).order_by('-fecha_publicacion')  
    
    # Paginación 
    paginator = Paginator(comentarios_list, 3)  
    page_number = request.GET.get('page')  
    comentarios = paginator.get_page(page_number)  

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            
            if request.user.is_authenticated:
                comentario.autor = request.user  
                comentario.save()
                return redirect('postindividual', post_id=post.id) 
            else:
                return redirect('login')  
    else:
        form = ComentarioForm()  

    return render(request, 'postindividual.html', {
        'post': post,
        'comentarios': comentarios,  
        'form': form
    })


# VISTA PARA FORMULARIO DE REGISTRO

def registrouser(request):
    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('posts')  
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

class CustomLogoutView(LogoutView):
    next_page = 'posts'  


# VISTA PARA LOGIN

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts')  
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

# VISTA PARA CONTACTANOS

def contactanos_view(request):
    return render(request, 'contacto.html')

