from django.contrib import admin

from movies.models import Movie


# Register your models here.
#search_fields,list_display는 예약어이다.
@admin.register(Movie) #관리자 사이트에 Movie 모델을 등록시키는 역할을 합니다.
class MovieAdmin(admin.ModelAdmin):
    #관리자 페이지에서 보여주고자하는 컬럼들을 열거합니다.
    list_display = ('movieCd','movieNm','prdtYear','nationAlt','openDt','repGenreNm')
    #필드 겁색시 찾아보고자 하는 컬럼 목록을 명시
    search_fields = ('movieNm','movieNmEn','genreAlt')
# end class MovieAdmin(admin.ModelAdmin)
# movieCd,movieNm,movieNmEn,prdtYear,openDt,typeNm,prdtStatNm,nationAlt,genreAlt,repNationNm,repGenreNm