from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

#Categoria
class Categoria (models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    

#Posteo
class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False, verbose_name="Titulo")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha pub") 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    resumen = models.TextField(max_length=500, null=False, verbose_name="resumen")
    texto = models.TextField(null=False, verbose_name="Contenido")
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default='Sin categoria')
    imagen = models.ImageField(null=False, blank=True, upload_to='media')
    publicado = models.DateTimeField(default=timezone.now)




class Meta: 
    ordering = ('-publicado',)  
    
    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
        
        

# usuarios con atributos nuevos
class CustomUser(AbstractUser):
    icono = models.ImageField(upload_to="media/usuarios", null=True, blank=True, default="media/usuarios/default.png")
    descripcion = models.TextField(max_length=350)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
        


# comentarios
class Comentario(models.Model):
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=250, verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        


