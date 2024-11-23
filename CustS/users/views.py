
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import auth
from django.urls import reverse
from carts.models import Cart
from users.forms import ProfileForm, UserLoginForm,UserRegistrationForm
from .services import register_user, authenticate_user, logout_user
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user=form.instance
            auth.login(request,user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request,f"{user}, Вы успешно зарегистрировались и вошли в аккаунт!")
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context={
        "title":'Home-Регистрация',
        'form': form,
    }
    return render(request,'users/register.html',context)



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            
            session_key = request.session.session_key

            if user:
                auth.login(request,user)
                messages.success(request,f"{username}, Вы вошли в аккаунт!")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'title': "Home-Авторизация",
        'form':form
    }
    return render(request,'users/login.html',context)



@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,f" Вы вышли из аккаунта!")
    return HttpResponseRedirect(reverse('home'))  # Перенаправление на главную страницу после выхода



@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST,instance=request.user,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Профиль успешно обновлён!")
            return redirect('user:profile')
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': ',mainpage',
        'form':form,
    }
    return render(request,'users/profile.html',context)


def users_carts(request):
    return render(request, 'users/users_carts.html')