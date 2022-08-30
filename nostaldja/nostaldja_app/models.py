from django.db import models

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Fad(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200)
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fad')

    def __str__(self):
        return self.name