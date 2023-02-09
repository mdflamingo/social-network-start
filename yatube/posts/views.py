from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(requests):
    return HttpResponse('Список всех публикаций')

def post_detail(requests, post_id):
    return HttpResponse('Страница с одним постом {post_id}')
