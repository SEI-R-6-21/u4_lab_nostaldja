from django.db import models

# Create your models here.

class Decades(models.Model):
    name = models.CharField(max_length=100)
    star_year = models.CharField(max_length=30, default='none')
    end_year = models.CharField(max_length=30,  default='none')
    def __str__(self):
        return self.name

class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decades, on_delete=models.CASCADE, related_name='fad')
    def __str__(self):
        return self.name