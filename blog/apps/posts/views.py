from django.shortcuts import render
from .models import Post, Categoria
from django.core.paginator import Paginator

def posts(request):
    categorias = Categoria.objects.all()  
    selected_categoria = request.GET.get('categoria')  

    # Filtrar los posts
    if selected_categoria:
        posts = Post.objects.filter(categoria__nombre=selected_categoria)  
    else:
        posts = Post.objects.all()  

    # Paginación
    paginator = Paginator(posts, 9)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'index.html', {'posts': page_obj, 'categorias': categorias})

def quienessomos(request):
    return render(request, 'quienessomos.html')

