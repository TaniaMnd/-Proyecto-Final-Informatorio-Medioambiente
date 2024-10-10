from django.shortcuts import render
from .models import Post

def posts(request):
  posts = Post.objects.all()
  print(posts)
  return render(request, 'index.html', {'posts' : posts})

