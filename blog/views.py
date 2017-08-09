from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/Home.html', {'posts': posts})

def static_page(request, page_name):
    return render(request, 'blog/' + page_name + '.html')


# Create your views here.
