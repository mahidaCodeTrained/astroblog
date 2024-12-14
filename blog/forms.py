from .models import Comment
from django import forms


class Commenting(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)