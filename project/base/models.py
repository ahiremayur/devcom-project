import email
from unicodedata import name
from django.db import models

# Create your models here.
class take(models.Model):
    name = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    
    
