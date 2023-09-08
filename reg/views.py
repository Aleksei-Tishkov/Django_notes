from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login


def reg(request):
    if request.method == 'GET':
        return render(request, 'reg/reg.html')
    data = request.POST
    username = data.get('username')
    email = data.get("email")
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password1, password2 = data.get('password1'), data.get('password2')
    if username is None or first_name is None or last_name is None:
        return HttpResponse('<h3>Nonames are not allowed</h3>')
    elif email is None:
        return HttpResponse("<h3>We need to spam someone, provide us your email</h3>")
    elif password1 is None or password2 is None:
        return HttpResponse("<h3>Password?</h3>")
    elif password1 != password2:
        return HttpResponse("<h3>Passwords?</h3>")
    else:
        new_user = User()
        new_user.create_user(username, full_name, email, password1)
        return HttpResponse("<h3>Вы успешно зарегистрировались</h3>")


def login_page(request):
    if request.method == "GET":
        return render(request, "reg/login.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return HttpResponse("<h3>Пользователь с таким логином и паролем не найден</h3>")
            login(request, user)
            return HttpResponse("<h3>Вы успешно авторизованы</h3>")
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")