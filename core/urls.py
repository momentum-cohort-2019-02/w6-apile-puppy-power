from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.get_user_profile, name='user-profile'),
    path('postlink/<int:pk>', views.PostLinkDetailView.as_view(), name='postlink-detail'),
]
