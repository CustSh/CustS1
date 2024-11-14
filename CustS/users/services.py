from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_user(request):
    """
    Регистрация нового пользователя и его автоматический вход в систему, если форма корректна.
    Возвращает кортеж (boolean, form), где boolean - успешность регистрации,
    а form - форма для отображения ошибок (если они есть).
    """
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return True, form
    return False, form


def authenticate_user(request):
    """
    Аутентификация пользователя. При успешной проверке - вход в систему.
    Возвращает кортеж (boolean, form), где boolean - успешность входа,
    а form - форма для отображения ошибок (если они есть).
    """
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return True, form
    return False, form

def logout_user(request):
    """
    Выход из системы текущего пользователя.
    """
    logout(request)
