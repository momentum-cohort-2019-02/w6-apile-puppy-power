from django.contrib import admin
from core.models import PostLink, Comment, Vote, HashTag, User

# Register your models here.

@admin.register(PostLink)
class PostLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'post_url', 'slug')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Vote)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(HashTag)
class CommentAdmin(admin.ModelAdmin):
    pass


