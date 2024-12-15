from django.shortcuts import render
from blog.models import PostBlog, Comment  # Import your blog models for posts and comments

def user_profile(request):
    """
    View to display the user's profile with their posts and comments.
    """
    posts = PostBlog.objects.filter(author=request.user)  # Get posts by the logged-in user
    comments = Comment.objects.filter(author=request.user)  # Get comments by the logged-in user

    context = {
        'posts': posts,
        'comments': comments,
    }

    return render(request, 'dashboard/user_profile.html', context)