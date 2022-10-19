from django.db import models

# Create your models here.

class Artiste(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

class Song(models.Model) :
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.IntegerField()

class Lyric(models.Model) :
    song = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
