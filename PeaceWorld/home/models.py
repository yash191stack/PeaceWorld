from django.db import models

# Create your models here.

class PeaceWorld(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    message = models.TextField()
    is_updated = models.BooleanField(default=False)
    


   
