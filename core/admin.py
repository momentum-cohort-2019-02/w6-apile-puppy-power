from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import PostLink, HashTag, Comment, Vote
from django.contrib.auth.models import User

# Register your models here.

@admin.register(PostLink)
class PostLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_url', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(HashTag)
admin.site.register(Vote)




