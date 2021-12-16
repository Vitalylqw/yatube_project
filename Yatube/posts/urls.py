# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страницы сообществ
    path('group_list/', views.group_list),


]
