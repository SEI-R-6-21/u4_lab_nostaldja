from django.db import models

# Create your models here.


class Decades(models.Model):
    """decades model"""
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fads(models.Model):
    """fads model"""
    decade = models.ForeignKey(
        Decades, on_delete=models.CASCADE, related_name='decade')
    name = models.CharField(max_length=100)
    imague_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
