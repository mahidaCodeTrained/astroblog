from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from .models import PostBlog

def fetchblog(request):
    # Fetch posts that are not drafts
    posts = PostBlog.objects.filter(status=1)
    
    # Set pagination: 6 posts per page (simulate paginate_by)
    paginator = Paginator(posts, 6)  # 6 posts per page
    
    # Get the current page number from the request's GET parameter
    page_number = request.GET.get('page')
    
    # Get the posts for the current page
    page_obj = paginator.get_page(page_number)
    
    # Return the response with the paginated posts
    return render(request, 'blog/index.html', {'page_obj': page_obj})