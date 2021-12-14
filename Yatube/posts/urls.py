# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страницы сообществ
    path('group/', views.group),
    # Страница сообщества
    path('group/<slug:slug>/', views.group_posts),

]
