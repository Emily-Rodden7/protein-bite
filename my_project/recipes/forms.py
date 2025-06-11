
from django import forms
from .models import Comment

# comment section for the recipes

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        