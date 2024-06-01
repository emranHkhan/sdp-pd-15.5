from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from musician.models import Musician

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    rating = models.IntegerField( validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

    def __str__(self):
        return self.album_name
