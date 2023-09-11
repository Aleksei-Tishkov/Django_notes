from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        f_name = request.user.first_name
        l_name = request.user.last_name
    else:
        f_name = None
        l_name = None
    return render(request, 'home/home.html', context={'first_name': f_name, 'last_name': l_name})