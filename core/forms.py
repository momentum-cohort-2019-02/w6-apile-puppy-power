from django import forms
from django.forms import ModelForm


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, help_text="Enter username")

    def validate_username(self):
        data = self.username

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'post_link', 'user',) 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

