from django.shortcuts import render
from blog.models import PostBlog, Comment  
from blog.models import PostSave 

def user_profile(request):
    """
    View to display the user's profile with their posts, comments, and saved posts.
    """
    posts = PostBlog.objects.filter(author=request.user)  # Get posts by the logged-in user
    comments = Comment.objects.filter(author=request.user)  # Get comments by the logged-in user
    
    
    saved_posts = PostSave.objects.filter(user=request.user).values_list('post', flat=True)
    posts_saved = PostBlog.objects.filter(id__in=saved_posts)
    
    context = {
        'posts': posts,
        'comments': comments,
        'saved_posts': posts_saved, 
    }

    return render(request, 'dashboard/user_profile.html', context)
