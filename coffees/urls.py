from django.urls import path

from  .views import *

app_name = 'coffees'

#파일이름: coffees/urls.py
urlpatterns = [
    #http://127.0.01:8000/coffees/chart01
   path('chart01', coffee_chart_01, name='coffee_chart_01'), #전체 데이터 보기
   # http://127.0.01:8000/coffees/chart03
   path('chart03', coffee_chart_03, name='coffee_chart_03'),

]
