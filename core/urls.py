from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.get_user_profile, name='user-profile'),
]
