from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.catalog,name='catalog'),
   path('<int:article>',views.clickedProduct,name='article')
]
