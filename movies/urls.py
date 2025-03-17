from django.urls import path

from  . import views

app_name = 'movies'

#파일이름: movies/urls.py
urlpatterns = [
path('', views.index),
    #http://127.0.01:8000/movies/movie_list_all
    #movies/all이라고 요청이 들어오면, movie_list_all 함수가 호출이 됩니다.
path('movie_list_all', views.movie_list_all, name='movie_list_all'), #전체 데이터 보기

#http://127.0.01:8000/movies/paginator
path('paginator', views.movie_list_paginator, name='movie_list_paginator'), #페이징 처리 내역 보기

#http://127.0.01:8000/movies/genre_chart_01
path('genre_chart_01', views.get_genre_count, name='genre/chart01'), #영화 장르별 집계

]
# movie_list_paginator는 view에 있는 함수와 동일해야된다.