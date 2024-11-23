from django.contrib import admin
from .models import Category, Product, Video

# Создаем инлайн для модели Video
class VideoInline(admin.TabularInline):  # Можно использовать admin.StackedInline для другого стиля отображения
    model = Video
    extra = 1  # Количество пустых полей для добавления новых видео

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]

from .models import SubCategory, SubClass

admin.site.register(SubCategory)
admin.site.register(SubClass)