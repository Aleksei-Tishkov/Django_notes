from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
#from models import User
from reg.models import User


def reg(request):
    if request.method == 'GET':
        return render(request, 'reg/reg.html')
    data = request.POST
    username = data.get('username')
    email = data.get("email")
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password1, password2 = data.get('password1'), data.get('password2')
    if not username or not first_name or not last_name:
        return render(request, 'reg/reg_other.html', context={'response': 'Please enter your first and last names'})
    elif not email:
        return render(request, 'reg/reg_other.html', context={'response': 'We need to spam someone, provide us your email'})
    elif password1 is None or password2 is None:
        return render(request, 'reg/reg_other.html', context={'response': 'Password?'})
    elif password1 != password2:
        return render(request, 'reg/reg_other.html', context={'response': 'Passwords?'})
    else:
        new_user = User()
        print(email)
        new_user.create_user(username, first_name, last_name, email, password1)
        return render(request, 'reg/reg_other.html', context={'response': 'Congrats! You can add your notes now!'})


def login_page(request):
    if request.method == "GET":
        return render(request, "reg/login.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return render(request, 'reg/reg_other.html', context={'response': 'There is no such user'})
            login(request, user)
            return render(request, 'reg/reg_other.html', context={'response': 'Yay! Welcome back!'})
        except KeyError:
            return render(request, 'reg/reg_other.html', context={'response': "Huh? We didn't get all the needed info, try again, pls"})


def logout_page(request):
    logout(request)
    return render(request, 'reg/reg_other.html', context={'response': 'Good-bye, sweet prince'})