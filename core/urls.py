from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('postlink/<int:pk>', core_views.PostLinkDetailView.as_view(), name='postlink-detail'),
    path('postlink/<int:pk>/vote/', core_views.postlink_vote_view,
    name="postlink-vote"),
    path('profile/<username>', core_views.get_user_profile, name="user-profile"),
    path('postlink/<int:pk>/comments/', core_views.new_comment, name="new_comment"),
    path('post/new/', core_views.add_post, name='add_post'),
]