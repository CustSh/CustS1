from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def catalog (request):
    products = Product.objects.all()
    return render(request,"catalog/catalog.html", {'products': products})



# def clickedProduct(request, article):
#     template_name = f'article{article}.html'
#
#     try:
#         template = get_template(template_name)
#     except TemplateDoesNotExist:
#         raise Http404("Страница не найдена")
#
#     return render(request, template_name)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

