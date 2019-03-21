from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postlink/<int:pk>', views.PostLinkDetailView.as_view(), name='postlink-detail'),
]
