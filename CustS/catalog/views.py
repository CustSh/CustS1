from django.http import Http404, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
def catalog(request, category_slug):
    page = request.GET.get('page', 1)  # текущая страница
    on_sale = request.GET.get('on_sale',None)
    order_by = request.GET.get('order_by',None)

    if category_slug == "all":
        products = Product.objects.all()
    else:
        products = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    if on_sale:
        products=products.filter(discount__gt=0)#to do фильтры по цене работают некорректно, дубляж блоков
    if order_by and order_by != "default":
        products=products.order_by(order_by)

    paginator = Paginator(products, 10)  # по 5 товаров на страницу
    current_page = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # проверка на AJAX
        products_data = [
            {
                "name": product.name,
                "price": product.price,
                "slug": product.slug,
                "image_url": product.image.url if product.image else None,
            }
            for product in current_page
        ]
        return JsonResponse({
            'products': products_data,
            'has_next': current_page.has_next(),
        })

    context = {
        "title": "Каталог товаров",
        "products": current_page,  # передаем только текущую страницу
        "slug_url": category_slug,
    }
    return render(request, "catalog/catalog.html", context)




# def clickedProduct(request, article):
#     template_name = f'article{article}.html'
#
#     try:
#         template = get_template(template_name)
#     except TemplateDoesNotExist:
#         raise Http404("Страница не найдена")
#
#     return render(request, template_name)

def product_detail(request, product_slug):
    product = get_object_or_404(Product,slug=product_slug)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)

