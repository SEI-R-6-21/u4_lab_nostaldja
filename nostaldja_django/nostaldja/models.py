from django.db import models

# Create your models here.
class Decades(models.Model):
  name = models.CharField(max_length=100)
  start_year = models.CharField(max_length=4)
  end_year = models.CharField(max_length=4)

  def __str__(self):
    return self.name

class Fads(models.Model):
  decade = models.ForeignKey(Decades, on_delete=models.CASCADE, related_name='fads')
  name = models.CharField(max_length=100)
  image_url = models.TextField(max_length=200)
  description = models.CharField(max_length=300)
  
  def __str__(self):
      return self.name