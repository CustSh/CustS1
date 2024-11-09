from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.catalog,name='catalog'),
   #path('<int:article>',views.clickedProduct,name='article'),
   path('<int:product_id>/', views.product_detail, name='product_detail'),
]
