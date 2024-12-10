from django.contrib import admin
from .models import Game, Buyer  # Импортируем модели

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение количества записей до 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    fields = ('name', 'balance', 'age')  # Убедитесь, что поле включено
    list_display = ('name', 'balance', 'age')  # Отображение полей name, balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение количества записей до 30
    readonly_fields = []
