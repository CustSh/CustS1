from django.shortcuts import render
from django.http import HttpResponse

def carts(request):
    return render(request, "carts/carts.html")

def add(request, product_id):
    return HttpResponse(status=204)

def change(request, product_id):
    return HttpResponse(status=204)

def remove(request, product_id):
    return HttpResponse(status=204)