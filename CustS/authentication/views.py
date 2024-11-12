from django.shortcuts import render, redirect
from .services import register_user, authenticate_user, logout_user


def register(request):
    success, form = register_user(request)
    if success:
        return redirect('home')  # Перенаправление на главную страницу после успешной регистрации
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    success, form = authenticate_user(request)
    if success:
        return redirect('home')  # Перенаправление на главную страницу после успешного входа
    return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    logout_user(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода
