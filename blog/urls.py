from django.urls import path
from . import views

urlpatterns = [
    # Place the profile URL first to avoid conflict with the post detail URLs
    path('', views.FetchBlog.as_view(), name='blog-home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('<slug:slug>/', views.detailed_posts, name='detailed_posts'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.edits, name='edits'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.deletion, name='delete_comment'),
    path('<slug:slug>/save_post/', views.save_post, name='save_post'),
    path('<slug:slug>/unsave_post/', views.unsave_post, name='unsave_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]


