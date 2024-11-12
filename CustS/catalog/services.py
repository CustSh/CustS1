from django.shortcuts import get_object_or_404
from .models import Product

def get_all_products():
    """
    Получает список всех продуктов.
    """
    return Product.objects.all()

def get_product_by_id(product_id):
    """
    Получает продукт по его ID или возвращает 404, если продукт не найден.
    """
    return get_object_or_404(Product, id=product_id)

