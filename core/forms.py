from django import forms
from django.forms import ModelForm
from core.models import PostLink, Vote, Comment, HashTag



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'postlink_detail', 'user',) 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

