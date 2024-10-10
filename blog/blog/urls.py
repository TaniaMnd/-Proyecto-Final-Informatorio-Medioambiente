
from django.contrib import admin
from django.urls import path, include
from apps.posts.views import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', posts, name='posts'),
    #path('posts/', include('apps.posts.urls')),
]
