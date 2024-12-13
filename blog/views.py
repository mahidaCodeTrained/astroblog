from django.shortcuts import render
from django.views import generic
from .models import PostBlog

def home(request):
    posts = PostBlog.objects.all()  # Fetch all blog posts
    return render(request, 'blog/post_list.html', {'posts': posts})