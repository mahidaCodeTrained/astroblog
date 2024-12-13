from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetchblog.as_view(), name='blog-home'),  # Homepage now points to post_list.html
]