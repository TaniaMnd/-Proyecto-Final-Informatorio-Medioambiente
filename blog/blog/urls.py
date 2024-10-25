from django.contrib import admin
from django.urls import path, include
from apps.posts.views import posts
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('enfoque_2024_admin/', admin.site.urls),
    path('', include('apps.posts.urls')), 
    path ('', posts, name='posts'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




