from django.urls import path,include
from . import views


app_name = 'catalog'

urlpatterns = [
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),

]