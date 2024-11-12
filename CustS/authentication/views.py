# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную после входа
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную после выхода
