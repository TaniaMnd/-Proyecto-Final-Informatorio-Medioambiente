from django.urls import path
from .views import posts, quienessomos

urlpatterns = [
    path ('', posts, name = 'posts'),
    path('quienessomos/', quienessomos, name='quienessomos'), 
]


