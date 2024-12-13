from django.shortcuts import render
from django.views import generic
from .models import PostBlog

class FetchBlog(generic.ListView):
    model = PostBlog
    template_name = "blog/index.html"
    paginate_by = 6  # 6 posts per page

