from django.urls import path
from . import views

urlpatterns = [
    path('posts/<slug:post_id>/', views.post_detail),
    path('posts/', views.group_posts),
    path('', views.index),
]