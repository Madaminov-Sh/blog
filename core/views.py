from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
    

def detailView(request, slug):
    post = get_object_or_404(Post, slug = slug)
    context = {
        'post': post
    }
    return render(request, 'about.html', context = context)