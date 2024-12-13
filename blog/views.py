from django.shortcuts import render
from django.views import generic
from .models import PostBlog

class fetchblog(generic.ListView):
    # Fetch posts that are not drafts
    queryset = PostBlog.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    