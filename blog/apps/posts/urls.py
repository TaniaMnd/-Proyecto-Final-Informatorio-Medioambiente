from django.urls import path
from .views import posts, quienessomos, postindividual

urlpatterns = [
    path ('', posts, name = 'posts'),
    path('quienessomos/', quienessomos, name='quienessomos'), 
    path('post/<int:post_id>/', postindividual, name='postindividual'),
]


