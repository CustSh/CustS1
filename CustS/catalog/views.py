from django.shortcuts import render
from .services import get_all_products, get_product_by_id, search_products


def catalog(request):
    query = request.GET.get('q')

    # Если запрос пустой, просто возвращаем страницу без изменений
    if not query or query.strip() == "":
        return render(request, "main/mainpage.html", {'query': query})

    # Выполняем поиск, если запрос не пустой
    products = search_products(query)
    return render(request, "catalog/catalog.html", {'products': products, 'query': query})

def product_detail(request, product_id):
    product = get_product_by_id(product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})


