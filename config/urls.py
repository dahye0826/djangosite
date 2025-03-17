"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from config.views import home
from movies import views

#파일이름: config/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    # path('movies/', views.index), # movies 앱의 index 함수 호출
    path('movies/', include('movies.urls')),  # movies 앱의 urls 파일 포함시키기
    path('coffees/', include('coffees.urls')),
]
