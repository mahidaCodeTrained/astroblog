from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import PostBlog, Comment, PostSave
from .forms import Commenting, PostForm

class FetchBlog(generic.ListView):
    model = PostBlog
    template_name = "blog/index.html"
    paginate_by = 6
    
    def get_queryset(self):
        # Filter to show only published posts
        return PostBlog.objects.filter(status=1)  # Show only published posts


def detailed_posts(request, slug):
    """
    Display an individual :model:`blog.PostBlog`.
    
    **Context**
    ``post``: An instance of :model:`blog.PostBlog`.
    
    **Template:** :template:`blog/detailed_posts.html`
    """
    
    # Fetch the post based on the slug (this ensures `post` is defined)
    post = get_object_or_404(PostBlog, slug=slug)

    # Check if the post is a draft and if the logged-in user is the author
    if post.status == 0 and post.author != request.user:
        raise Http404("Post not found.")

    # Fetch comments for the post
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Handle comment submission
    if request.method == "POST":
        if request.user.is_authenticated:
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
        else:
            messages.warning(request, "You must be logged in to comment.")
            return redirect('login')  # Redirect unauthenticated users to the login page
    else:
        comment_form = Commenting()

    # Check if the user has already saved the post
    is_saved = PostSave.objects.filter(user=request.user, post=post).exists() if request.user.is_authenticated else False

    # Handle saving the post
    if request.method == "POST":
        if 'save_post' in request.POST:
            if request.user.is_authenticated:
                saved_post, created = PostSave.objects.get_or_create(user=request.user, post=post)
                if created:
                    messages.success(request, 'Post saved successfully!')
                else:
                    messages.info(request, 'You have already saved this post.')
            else:
                messages.warning(request, "You must be logged in to save a post.")
                return redirect('login')  # Redirect unauthenticated users to the login page
            
            return redirect('detailed_posts', slug=slug)  # Redirect back to the same post page

        # Handle unsaving the post
        elif 'unsave_post' in request.POST:
            if request.user.is_authenticated:
                PostSave.objects.filter(user=request.user, post=post).delete()
                messages.success(request, 'Post unsaved successfully!')
            else:
                messages.warning(request, "You must be logged in to unsave a post.")
                return redirect('login')  # Redirect unauthenticated users to the login page
            
            return redirect('detailed_posts', slug=slug)

    # Render the detailed post page with the context
    return render(
        request,
        "blog/detailed_posts.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "is_saved": is_saved,  # Add this to check if the post is saved
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


@login_required
def create_post(request):
    """
    View to create a new post with the option to choose draft or published.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Associate the post with the logged-in user
            post.save()

            if post.status == 1:  # Published post
                messages.success(request, 'Your post has been created and is now published!')
            else:  # Draft post
                messages.success(request, 'Your post has been created and saved as a draft!')

            return redirect('blog-home')  # Redirect to the blog home page or another page
        else:
            messages.error(request, 'There was an error creating your post.')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(PostBlog, slug=slug)

    # Ensure that only the author of the post can edit it
    if post.author != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('blog-home')

    # If the form is submitted (POST request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()  # Save the edited post
            messages.success(request, "Your post has been updated successfully!")
            return redirect('detailed_posts', slug=post.slug)  # Redirect to the post's detail page
        else:
            messages.error(request, "There was an error updating your post.")
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, slug):
    """
    View to delete a post. Only the author can delete their own post.
    """
    # Get the post based on the slug
    post = get_object_or_404(PostBlog, slug=slug)

    # Check if the logged-in user is the author of the post
    if post.author != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('blog-home')

    # Delete the post
    post.delete()
    messages.success(request, "Your post has been deleted successfully!")
    
    # Redirect to the blog home or any other appropriate page
    return redirect('blog-home')


@login_required
def save_post(request, slug):
    """
    View to save a post.
    Redirects the user to their profile page after saving the post.
    """
    post = get_object_or_404(PostBlog, slug=slug)
    saved_post, created = PostSave.objects.get_or_create(user=request.user, post=post)
    
    if created:
        messages.success(request, 'Post saved successfully!')
    else:
        messages.info(request, 'You have already saved this post.')
    
    return HttpResponseRedirect(reverse('user_profile'))  # Redirect to profile page

@login_required
def unsave_post(request, slug):
    """
    View to unsave a post.
    Redirects the user to their profile page after unsaving the post.
    """
    post = get_object_or_404(PostBlog, slug=slug)
    
    # Deleting the saved post from the user's saved posts
    PostSave.objects.filter(user=request.user, post=post).delete()
    
    messages.success(request, 'Post unsaved successfully!')

    return HttpResponseRedirect(reverse('user_profile'))  # Redirect to profile page
