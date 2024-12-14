from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchBlog.as_view(), name='blog-home'),
    path('<slug:slug>/', views.detailed_posts, name='detailed_posts'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.edits, name='edits'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.deletion, name='deletion')
]