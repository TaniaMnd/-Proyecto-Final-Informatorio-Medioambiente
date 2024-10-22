from django.contrib import admin
from django.urls import path, include
from .views import index


from django.conf import settings
from django.conf.urls.static import static 

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    #urls de apps posts
    path("posts/", include("Apps.posts.urls")),
    # si sumamos más apps
    path(
        "login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
