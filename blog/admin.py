from django.contrib import admin
from .models import PostBlog
from .models import Comment
# Register your models here.
admin.site.register(PostBlog)
admin.site.register(Comment)