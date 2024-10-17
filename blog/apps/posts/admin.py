from django.contrib import admin
from .models import Post, Categoria, Comentario, CustomUser


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'autor', 'resumen', 'texto', 'activo', 'categoria', 'imagen', 'publicado')

admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(CustomUser)


