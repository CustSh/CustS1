from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/',views.profile,name='profile'),
    path('users_carts/', views.users_carts, name='users_carts'),
]
