from django.contrib import admin

from .models import Post, Group


class PostsAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date', 'author',)
    list_editable = ('group',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(Post, PostsAdmin)


class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'name', 'slug', 'description')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name', 'description')
    # Добавляем возможность фильтрации по дате
    list_filter = ('slug',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)
