from django.db import models

# Create your models here.
class Decade(models.Model):
  name = models.CharField(max_length=100)
  start_year = models.DateField(auto_now=False,auto_now_add=False)
  end_year = models.DateField(auto_now=False,auto_now_add=False)

  def __str__(self):
    return self.name

class Fad(models.Model):
  name = models.CharField(max_length=100)
  image_url = models.TextField()
  description = models.CharField(max_length=100)
  decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

  def __str__(self):
    return self.name
