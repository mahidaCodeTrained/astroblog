from django.shortcuts import render
from django.views import generic
from .models import PostBlog

def fetchblog(request):
    # Fetch posts that are not drafts i'll use function based viewing instead of class based.
    posts = PostBlog.objects.filter(status=1)  
    return render(request, 'blog/post_list.html', {'posts': posts})