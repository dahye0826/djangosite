from django.db import models

# Create your models here.
#상속을 받을때는 models.Model를 쓴다./ 슈퍼클래스 model을 상속 받는다.
class Movie(models.Model):
    movieCd = models.CharField(max_length=10, primary_key=True)
    movieNm = models.CharField(max_length=255)
    movieNmEn = models.CharField(max_length=255, blank=True, null=True)
    prdtYear = models.IntegerField(default=0)
    openDt = models.CharField(max_length=10, blank=True, null=True)
    typeNm = models.CharField(max_length=50)
    prdtStatNm = models.CharField(max_length=50)
    nationAlt = models.CharField(max_length=255)
    genreAlt = models.CharField(max_length=255, null=True)
    repNationNm = models.CharField(max_length=50)
    repGenreNm = models.CharField(max_length=50)

    # 장고에 설계되어있다.
    class Meta:
        db_table='movies' #테이블 이름 지정/

    def __str__(self): #자바의 tostring()과 유사
        return self.movieNm

    # end class Meta

#end class movie