from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalog.models import Product
from carts.models import Cart

# работает
def carts(request):
    return render(request, "carts/carts.html", {'request': request})

# работает
# def carts(request):
#     carts = Cart.objects.filter(user=request.user) if request.user.is_authenticated else None
#     context = {
#         'carts': carts,
#     }
#     return render(request, 'carts/carts.html', context)


def add(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])

def change(request, product_slug):
    return HttpResponse(status=204)

def remove(request, product_slug):
    return HttpResponse(status=204)
