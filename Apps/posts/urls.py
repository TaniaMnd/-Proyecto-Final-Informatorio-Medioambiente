# urls solo de la app posts
from django.urls import path
from . import views
from .views import contactanos_view  # Conserva solo esta línea

urlpatterns = [
    path("", views.posts, name="noticias"),
    path("quienessomos/", views.about_us, name="quienessomos"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("detalle/<int:id>", views.post_id, name="detalle"),
    path('contactanos/', contactanos_view, name='contactanos'),
]


 