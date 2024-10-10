from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria, Comentario
from django.core.paginator import Paginator
from .form import ComentarioForm


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


#vista para quienes somos
def quienessomos(request):
    return render(request, 'quienessomos.html')


# Vista para mostrar un post específico y manejar comentarios
def postindividual(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(post=post).order_by('-fecha_publicacion')  

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user  
            comentario.save()
            return redirect('postindividual', post_id=post.id) 
    else:
        form = ComentarioForm()

    return render(request, 'postindividual.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })


