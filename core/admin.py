from django.contrib import admin
from core.models import PostLink, HashTag, Comment, Vote

# Register your models here.

@admin.register(PostLink)
class PostLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_url', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(HashTag)
admin.site.register(Vote)
