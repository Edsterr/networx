from django.conf.urls import url, include, re_path
from django.contrib import admin
from app import views

"""networx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('login/register', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile_id_func, name='profile'),
    path('profile/<int:profile_id>/', views.profile_id_func, name='profile_id_func'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]
