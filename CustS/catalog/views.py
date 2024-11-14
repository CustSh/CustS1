from django.shortcuts import render
from .services import get_all_products, get_product_by_id, search_products

def catalog(request):
    query = request.GET.get('q')  # Получаем поисковый запрос
    if query:
        products = search_products(query)  # Поиск продуктов по запросу
    else:
        products = get_all_products()  # Все продукты, если нет запроса
    return render(request, "catalog/catalog.html", {'products': products, 'query': query})

def product_detail(request, product_id):
    product = get_product_by_id(product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})


