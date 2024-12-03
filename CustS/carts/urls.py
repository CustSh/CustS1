from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.carts, name='carts'),
    path('add/', views.add, name='add'),
    path('change/', views.change, name='change'),
    path('remove/', views.remove, name='remove'),
]
