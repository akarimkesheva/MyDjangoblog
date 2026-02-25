from django import forms
from .models import Post, Comment  # Check that Comment is added here!

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):  # Ensure there is a colon (:) here!
    class Meta:
        model = Comment
        fields = ('author', 'text',)