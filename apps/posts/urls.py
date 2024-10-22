# urls solo de la app posts
from django.urls import path, include
from . import views
from .views import contactanos_view  
from .views import nuevo_post
from .views import eliminar_post
from .views import agregar_comentario
from .views import eliminar_comentario 
from .views import modificar_post
from .views import modificar_post, post_id
from .views import Modificar_Comentario


urlpatterns = [
    path("", views.posts, name="noticias"),
    path("quienessomos/", views.about_us, name="quienessomos"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("postindividual/<int:id>/", views.post_id, name="postindividual"),
    path('post/<int:post_id>/comentario/', agregar_comentario, name='agregar_comentario'),
    path('contactanos/', contactanos_view, name='contactanos'),
    path('nuevo_post/', nuevo_post, name='nuevo_post'),
    path('posts/eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
    path('comentarios/eliminar/<int:comentario_id>/', eliminar_comentario, name='eliminar_comentario'),
    path('modificar_post/<int:id>/', modificar_post, name='modificar_post'),
    path('<int:id>/', post_id, name='postindividual'),
    path('modificar_comentario/<int:pk>/', Modificar_Comentario.as_view(), name='modificar_comentario'),   
]


 