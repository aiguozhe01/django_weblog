from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post # from models.py, import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # overriding the default name object_list instead of post.
    ordering = ['-date_posted'] # argument to order the posts.

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})