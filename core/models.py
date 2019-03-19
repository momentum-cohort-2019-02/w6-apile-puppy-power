from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from autoslug import AutoSlugField


User = get_user_model()

class HashTag(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

class PostLink(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_url = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = AutoSlugField(populate_from='title', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostLink-detail', args=[str(self.id)])

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostLink, on_delete=models.CASCADE)
    voted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment = models.TextField(max_length=255)
    post = models.ForeignKey(PostLink, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return f'{self.id} ({self.PostLink.title})'


# adding comment for git training. :) 

