from django.contrib import admin
from django.db import models

# Create your models here.
from django.utils import timezone
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    subject = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    create_date = models.DateField(default=timezone.now)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)