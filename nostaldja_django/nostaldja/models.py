from django.db import models

# Create your models here.


class Decade(models.Model):
    name = models.CharField(max_length=100, default='no decade name')
    start_year = models.CharField(max_length=100, default='no decade start year')
    end_year = models.CharField(max_length=100, default='no decade end year')

    def __str__(self):
      return self.name


class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='Fads')
    name = models.CharField(max_length=100, default='no fad name')
    image_url = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, default='no fad description')


    def __str__(self):
      return self.name
    
