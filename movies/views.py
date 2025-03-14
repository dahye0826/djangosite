from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


# Create your views here.
def index(request):
    return HttpResponse('안녕하세요. 마이 페이지에 오신 것을 환영합니다. ')
#end def index(request)

# 모든 영화 목록을 보여 줍니다.
def movie_list_all(request):
    #영화를 prtYear의 역순으로 정렬하여 전체를 가져옵니다.
    movie_list = Movie.objects.order_by('-prdtYear')
    context = {'movie_list':movie_list}

    # request 영역에 context을 담아 보낼테니,movie/movie_list_all.html 에서 렌더링 해주세요
    return render(request,'movies/movie_list_all.html', context)
#end def movie_list_all(request):