from email.mime import image
from statistics import mode
from tkinter import CASCADE
from tracemalloc import start
from unicodedata import name
from django.db import models

# Create your models here.


# DECADE MODEL
class Decade(models.Model):
    name = models.CharField(max_length=50)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name

# FAD MODEL


class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=CASCADE, related_name='fads')
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
