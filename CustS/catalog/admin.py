from django.contrib import admin
from .models import Category, Product, Video

# Создаем инлайн для модели Video
class VideoInline(admin.TabularInline):  # Можно использовать admin.StackedInline для другого стиля отображения
    model = Video
    extra = 1  # Количество пустых полей для добавления новых видео

# Регистрируем модель Product с добавлением инлайновой модели Video
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

# Регистрируем модель Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
