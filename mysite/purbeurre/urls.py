"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

app_name = 'purbeurre'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('creation_successful/', views.creation_successful, name='creation_successful'),
    path('search_result/', views.search_result, name='search_result'),
    path('<int:food_id>/', views.food_page, name='food_page'),
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('fav_added/', views.fav_added, name='fav_added'),
    path('legal/', views.legal, name='legal'),
]
