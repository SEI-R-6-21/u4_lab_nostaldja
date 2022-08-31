from django.db import models

# Create your models here.


class Decades(models.Model):

    name = models.CharField(max_length=20)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name


class Fads(models.Model):

    name = models.CharField(max_length=80)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(
        Decades, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name
