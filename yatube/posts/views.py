from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return HttpResponse('Это главная страница')

def group_posts(requests):
    return HttpResponse('Список всех публикаций')

def post_detail(requests, post_id):
    return HttpResponse('Страница с одним постом {post_id}')
