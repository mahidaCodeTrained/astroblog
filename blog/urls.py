from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchBlog.as_view(), name='blog-home'),  
]