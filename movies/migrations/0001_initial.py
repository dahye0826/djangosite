# Generated by Django 3.1.3 on 2025-03-14 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieCd', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('movieNm', models.CharField(max_length=255)),
                ('movieNmEn', models.CharField(blank=True, max_length=255, null=True)),
                ('prdtYear', models.IntegerField(default=0)),
                ('openDt', models.CharField(blank=True, max_length=10, null=True)),
                ('typeNm', models.CharField(max_length=50)),
                ('prdtStatNm', models.CharField(max_length=50)),
                ('nationAlt', models.CharField(max_length=255)),
                ('genreAlt', models.CharField(max_length=255, null=True)),
                ('repNationNm', models.CharField(max_length=50)),
                ('repGenreNm', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
