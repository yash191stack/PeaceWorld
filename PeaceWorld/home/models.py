# from django.db import models

# # Create your models here.

# class PeaceWorld(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=50)
#     phone_num = models.CharField(max_length=15)
#     message = models.TextField()
#     is_updated = models.BooleanField(default=False)
    

# ✅ Updated models.py
from django.db import models
import uuid

class PeaceWorld(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    message = models.TextField()
    is_updated = models.BooleanField(default=False)
    secret_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # 👈 Anonymous ownership

    def __str__(self):
        return self.name

