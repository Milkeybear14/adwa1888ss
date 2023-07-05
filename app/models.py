from django.db import models

# Create your models here.
class what_we_do(models.Model):
    image = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length = 50)
    link_name= models.CharField(max_length = 50)
    paragraph = models.TextField()
class why_choose_us(models.Model):
    title = models.CharField(max_length = 50)
    paragraph = models.TextField()
class clients_response(models.Model):
    image = models.ImageField(upload_to = 'pics')
    paragraph = models.TextField()
    title = models.CharField(max_length = 50)
class year(models.Model):
    title = models.CharField(max_length=4)