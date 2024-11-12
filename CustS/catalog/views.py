# catalog/views.py
from django.shortcuts import render
from .services import get_all_products, get_product_by_id

def catalog(request):
    products = get_all_products()
    return render(request, "catalog/catalog.html", {'products': products})

def product_detail(request, product_id):
    product = get_product_by_id(product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})
