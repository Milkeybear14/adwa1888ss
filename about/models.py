from django.db import models

# Create your models here.
class about_company(models.Model):
    title = models.CharField(max_length = 50)
    paragraph = models.TextField()
class contact(models.Model):
    location = models.CharField(max_length = 80)
    phone_number = models.CharField(max_length = 15)
    email = models.EmailField()