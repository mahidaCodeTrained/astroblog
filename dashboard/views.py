from django.shortcuts import render
from blog.models import PostBlog, Comment, PostSave


def user_profile(request):
    posts = PostBlog.objects.filter(author=request.user)
    comments = Comment.objects.filter(author=request.user)
    saved_posts = PostSave.objects.filter(user=request.user).values_list(
        'post', flat=True
    )
    posts_saved = PostBlog.objects.filter(id__in=saved_posts)

    context = {
        'posts': posts,
        'comments': comments,
        'saved_posts': posts_saved,
    }

    return render(request, 'dashboard/user_profile.html', context)
