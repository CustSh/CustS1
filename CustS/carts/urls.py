from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.carts, name='carts'),
    path('add/<slug:product_slug>/', views.add, name='add'),
    path('change/<slug:product_slug>/', views.change, name='change'),
    path('remove/<int:cart_id>/', views.remove, name='remove'),
]
