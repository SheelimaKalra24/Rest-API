from django.db import models

# Create your models here.
class post(models.Model):
  title = models.CharField(max_length=255)
  des = models.CharField(max_length=255)
  image = models.ImageField(upload_to='media/') 

  def __str__(self):
    return self.title
  

