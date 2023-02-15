from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/group/<slug>/', views.post_detail, name='post_detail'),
    path('posts/', views.group_posts, name='group_list'),
    path('', views.index, name='index'),
]