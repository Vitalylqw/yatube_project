# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group(request):
    return HttpResponse('Список групп')


def group_posts(request, slug):
    return HttpResponse(f'Группа {slug}')
