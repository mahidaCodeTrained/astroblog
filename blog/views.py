from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import PostBlog, Comment
from .forms import Commenting

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
    if request.method == "POST":
        comment_form = Commenting(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and is now waiting approval!'
    )
    
    comment_form = Commenting()

    return render(
    request,
    "blog/detailed_posts.html",
    {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
)

def edits(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = PostBlog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = Commenting(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated at Astroblog!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('detailed_posts', args=[slug]))


def deletion(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = PostBlog.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted at Astroblog!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('detailed_posts', args=[slug]))
