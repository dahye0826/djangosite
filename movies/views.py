from re import search

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


# Create your views here.
def index(request):
    return HttpResponse('안녕하세요. 마이 페이지에 오신 것을 환영합니다. ')
#end def index(request)

# 모든 영화 목록을 보여 줍니다.
def movie_list_all(request):
    # 영화를 prdtYear의 역순으로 정렬하여 전체를 가져 옵니다.
    movie_list = Movie.objects.order_by('-prdtYear')
    context = {'movie_list': movie_list}

    # request 영역에 context을 담아 보낼테니, movie_list_all.html에서 렌더링해주세요.
    return render(request, 'movies/movie_list_all.html', context)
# end def movie_list_all(request):

# sqlite에서 테이블 구조 확인하는 방법
# PRAGMA table_info(movies);
'''
SELECT * FROM movies
ORDER BY openDt DESC
LIMIT 10 OFFSET 10;

SELECT * FROM movies
ORDER BY openDt DESC
LIMIT 10 OFFSET 20;
'''


# 페이징 처리를 사용하여 영화 목록을 10개씩 보여 줍니다.
def movie_list_paginator(request):
    #post 방식은 request.Post.get('파라미터 이름')으로 사용합니다.
    search_type = request.GET.get('search_type') # 검색 필드
    search_value = request.GET.get('search_value') #검색하고자 하는 값
    page = request.GET.get('page',1)  #현재 페이지(기본값:1) #url 에서 페이지 인식

    #models애 있는 Movie
    movies = Movie.objects.all()

    #검색 필터 적용
    '''
    filter_args = {'a':100, 'b':200}
    # 키워드 인수 언패킹
    movies = movies.filter(**filter_args)
    movies = movies.filter(a=100, b=200)와 동일한 개념
    '''

    #search_type and search_value 모두 존재하면
    if search_type and search_value :
        filter_args = {f'{search_type}__icontains': search_value} #템플릿 필터
        movies = movies.filter(**filter_args)
    #end if

    movies = movies.order_by('-openDt')

    paginator = Paginator(movies,10)
    movies = paginator.get_page(page) # 현재 페이지에 있는 데이터를 가져옴
    context = {'movies':movies}


    # request 영역에 context을 담아 보낼테니,movie/movie_list_all.html 에서 렌더링 해주세요
    return render(request,'movies/movie_list_paginator.html', context)
#end def movie_list_paginator(request):

'''
select repGenreNm as item, count(*) as cnt from movies
where repGenreNm is not null and repGenreNm not in('성인물(에로)', '뮤지컬', '사극', '어드벤처')
group by repGenreNm
order by cnt desc ;
'''

def get_genre_count(request):
   results = (Movie.objects
               .values('repGenreNm') #repGenreNm 컬럼으로 그룹핑
               .exclude(repGenreNm__in=['성인물(에로)', '뮤지컬', '사극', '어드벤처'])
               .annotate(cnt=Count('repGenreNm')) #각 항목을 카운트
               .order_by('-cnt'))  #빈도수가 큰 것 부터 정렬
   print('조회된 데이터:', list(results)) #diango 콘솔에서 확인

   #데이터를 chart.js에서 사용하기 편리하도록 재가공
   items = [element['repGenreNm'] for element in results]
   counts = [element['cnt'] for element in results]
   print('items', items)
   print('counts', counts)

   context = {
       'items':items,
       'counts':counts
   }
   return render(request, 'movies/movie_genre_chart_01.html', context)



# end def get_genre_count(request):