from django.contrib import admin
from .models import PostBlog, Comment, PostSave
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostBlog)
class PostBlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(PostSave)
class PostSaveAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'saved_on')
    list_filter = ('saved_on',)
    search_fields = ('user__username', 'post__title')

# Register your models here.


admin.site.register(Comment)
