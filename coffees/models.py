from django.db import models

# Create your models here.

class Coffee(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField()
    district = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'coffees'

    # end class Meta

    def __str__(self):
        return f"{self.brand} - {self.name}"

    #정의만 했기때문에 python manage.py migrate를 해줘야 DB에 생성이 된다.

