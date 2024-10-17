from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria, Comentario
from django.core.paginator import Paginator
from .form import ComentarioForm, RegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden, HttpResponseRedirect


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

#Staff o superusuario
def is_staff(user):
    return user.is_staff or user.is_superuser

#Elimnar posteo
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


def postindividual(request, post_id, comentario_id=None, eliminar_id=None):
    post = get_object_or_404(Post, id=post_id)
    comentarios_list = Comentario.objects.filter(post=post).order_by('-fecha_publicacion')

    # Paginación
    paginator = Paginator(comentarios_list, 3)
    page_number = request.GET.get('page')
    comentarios = paginator.get_page(page_number)

    if comentario_id:
        comentario_a_editar = get_object_or_404(Comentario, id=comentario_id, post=post)
        if comentario_a_editar.autor != request.user and not request.user.is_staff:
            return HttpResponseForbidden("No podes editar este comentario")
        form = ComentarioForm(request.POST or None, instance=comentario_a_editar)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('postindividual', post_id=post.id)
    else:
        form = ComentarioForm(request.POST or None)

        if request.method == 'POST':
            if not request.user.is_authenticated:
                return HttpResponseRedirect(f'/login/?next={request.path}')

            if form.is_valid():
                nuevo_comentario = form.save(commit=False)
                nuevo_comentario.post = post
                nuevo_comentario.autor = request.user
                nuevo_comentario.save()
                return redirect('postindividual', post_id=post.id)

    if request.method == 'POST' and 'eliminar_id' in request.POST:
        eliminar_id = request.POST.get('eliminar_id')
        comentario_a_eliminar = get_object_or_404(Comentario, id=eliminar_id)
        if comentario_a_eliminar.autor == request.user or request.user.is_staff:
            comentario_a_eliminar.delete()
            return redirect('postindividual', post_id=post.id)
        else:
            return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")

    return render(request, 'postindividual.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
        'comentario_id': comentario_id,
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

