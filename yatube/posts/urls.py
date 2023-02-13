from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/<slug:post_id>/', views.post_detail, name='post_detail'),
    path('posts/', views.group_posts, name='group_posts'),
    path('', views.index, name='index'),
]