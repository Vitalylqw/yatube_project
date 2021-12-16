from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    context = {
        'title': 'Это главная страница проекта Yatube'
                }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)

