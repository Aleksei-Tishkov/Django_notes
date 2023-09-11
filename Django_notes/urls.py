"""
URL configuration for Django_notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home
from reg.views import reg, login_page, logout_page
from notes.views import add_note, view_notes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('reg/', reg),
    path('reg', reg),
    path('login/', login_page),
    path('login', login_page),
    path('logout/', logout_page),
    path('home/logout/', logout_page),
    path('home/login/', login_page),
    path('add_note/', add_note),
    path('add_note', add_note),
    path('notes/', view_notes),
    path('notes', view_notes),

]
