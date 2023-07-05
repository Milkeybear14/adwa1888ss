from django.db import models

# Create your models here.
class portfolios(models.Model):
    image = models.ImageField(upload_to = 'image')
    title = models.CharField(max_length = 50)
    link = models.URLField(max_length = 50)
    paragraph = models.TextField()