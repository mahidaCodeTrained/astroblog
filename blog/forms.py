from django import forms
from .models import PostBlog, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ['title', 'slug', 'content', 'featured_image', 'excerpt', 'status']

class Commenting(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)