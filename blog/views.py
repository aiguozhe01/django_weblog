from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 16, 2020'
    },
     {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 17, 2020'
    }
]

def home(request):
    context = {
        'posts':posts # key: value
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})