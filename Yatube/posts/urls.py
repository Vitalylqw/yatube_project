# posts/urls.py

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страницы сообществ
    path('group_list/', views.group_posts, name='group_list'),


]
