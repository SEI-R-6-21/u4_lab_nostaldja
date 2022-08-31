from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length='100', default='none'),
    start_year = models.CharField(max_length=4),
    end_year = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Fads(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads'),
    name = models.CharField(max_length=100, default='none'),
    image_url = models.TextField(),
    description = models.CharField(max_length=300),
    decade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
