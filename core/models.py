from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.

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
    topic = models.ManyToManyField(HashTag, blank=True)

    voted_by = models.ManyToManyField(to=User, related_name='voted_postlinks', through='Vote')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postlink-detail', args=(self.id,))

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postlink = models.ForeignKey(PostLink, on_delete=models.CASCADE)
    voted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment = models.TextField(max_length=255)
    postlink = models.ForeignKey(PostLink, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return reverse('postlink-detail', args=(self.id,))
