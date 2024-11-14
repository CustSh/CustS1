from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.carts, name='carts'),
    path('add/<int:product_id>/', views.add, name='add'),
    path('change/<int:product_id>/', views.change, name='change'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
]
