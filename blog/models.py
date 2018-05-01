from django.db import models
from django.urls import reverse 


# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  body = models.TextField()

  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])

  def __str__(self):
    return self.title

class Log(models.Model):
  title = models.CharField(max_length=200)
  publication = models.CharField(max_length=150)
  url = models.CharField(max_length=100)
  date = models.TimeField()
  body = models.TextField(max_length=1000)
