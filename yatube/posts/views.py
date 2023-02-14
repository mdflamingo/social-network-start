from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request):
    template = 'posts/group_posts.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': 'Группы проекта'
    }
    return render (request, template, context)

def post_detail(request, post_id):
    return render(f'kjdh{post_id}')

