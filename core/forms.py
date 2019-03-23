from django import forms
from django.forms import ModelForm
from core.models import PostLink, Comment, Vote, HashTag, User



class CommentForm(forms.ModelForm):
    model = Comment
    fields = ['post_comment']


class PostForm(forms.ModelForm):

    class Meta:
        model = PostLink
        fields = ('title', 'post_link', 'user',) 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
