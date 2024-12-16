from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import PostBlog, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = [
            'title', 'slug', 'content', 'featured_image', 'excerpt', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If editing an existing instance, remove the 'slug' field from the form
        if self.instance and self.instance.pk:  # Check if the instance exists (i.e., we are editing)
            del self.fields['slug']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Automatically generate the slug if it's not provided
        if not instance.slug:
            instance.slug = slugify(instance.title)

        if commit:
            instance.save()

        return instance

        

class Commenting(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)