from django.shortcuts import render, redirect
from django.contrib import auth
from users.forms import UserLoginForm
from .services import register_user, authenticate_user, logout_user


def register(request):
    success, form = register_user(request)
    if success:
        return redirect('home')  # Перенаправление на главную страницу после успешной регистрации
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'title': "Home-Авторизация",
        'form':form
    }
    return render(request,'users/login.html',context)

def user_logout(request):
    logout_user(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода

def profile(request):
    context = {
        'title': ',mainpage'
    }
    return render(request,'users/profile.html',context)
