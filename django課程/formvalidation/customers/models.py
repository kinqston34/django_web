from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30,blank=False,primary_key=True)
    email = models.EmailField(blank=False,null=False)
    tel = models.IntegerField(max_length=10)