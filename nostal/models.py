from django.db import models
from pyexpat import model


# Create your models here.


class Decade(models.Model):
    name = models.CharField(max_length=25)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name


class Fad(models.Model):
    name = models.CharField(max_length=25)
    image_url = models.TextField()
    description = models.CharField(max_length=450)
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
