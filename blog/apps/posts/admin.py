from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Categoria, Comentario, CustomUser

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'autor', 'resumen', 'activo', 'categoria', 'publicado')
    list_filter = ('activo', 'publicado', 'categoria', 'fecha')
    search_fields = ('titulo', 'resumen', 'autor__username')
    ordering = ('-fecha',)

admin.site.register(Categoria)
admin.site.register(Comentario)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('icono', 'descripcion')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('icono', 'descripcion')}),
    )