from django.urls import path, include
from core import views as core_views

# copied to copy

# urlpatterns = [
#     path('', core_views.index, name='index'),
#     path('postlink/<int:pk>', core_views.PostLinkDetailView.as_view(), name='postlinkdetail'),
#     # path('postlink/create/', views.PostLinkCreate.as_view(), name='postlink-create'),
#     # path('postlink/<slug:slug>/update/', views.PostLinkUpdate.as_view(), name='postlink_update'),
#     # path('postlink/<slug:slug>/delete/', views.PostLinkDelete.as_view(), name='postlink_delete'),
# ]
urlpatterns = [
    path('', views.index, name='index'),
    path('postlink/<int:pk>', views.PostLinkDetailView.as_view(), name='postlink-detail'),
    # path('postlink/create/', views.PostLinkCreate.as_view(), name='postlink-create'),
    # path('postlink/<slug:slug>/update/', views.PostLinkUpdate.as_view(), name='postlink_update'),
    # path('postlink/<slug:slug>/delete/', views.PostLinkDelete.as_view(), name='postlink_delete'),
]
