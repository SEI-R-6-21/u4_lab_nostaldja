from django.db import models

# Create your models here.
# tunr/models.py


class Decades(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)

    def __str__(self):
        return self.name


# tunr/models.py
class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField(max_length=200)
    decade = models.ForeignKey(
        Decades, on_delete=models.CASCADE, related_name='fad'
    )

    def __str__(self):
        return self.name
