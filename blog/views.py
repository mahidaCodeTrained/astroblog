from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import PostBlog

class FetchBlog(generic.ListView):
    model = PostBlog
    template_name = "blog/index.html"
    paginate_by = 6  # 6 posts per page


def detailed_posts(request, slug):
    """
    Display an individual :model:`blog.PostBlog`.

    **Context**

    ``post``
        An instance of :model:`blog.PostBlog`.

    **Template:**

    :template:`blog/detailed_posts.html`
    """

    queryset = PostBlog.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
    request,
    "blog/detailed_posts.html",
    {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
    },
)

