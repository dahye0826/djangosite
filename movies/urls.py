from django.urls import path

from  . import views

#파일이름: movies/urls.py
urlpatterns = [
path('', views.index),
path('all', views.movie_list_all),]
