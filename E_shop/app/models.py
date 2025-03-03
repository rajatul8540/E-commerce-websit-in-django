from django.db import models
from django.forms import CharField
# Create your models here.
class Categroy(models.Model):
    name = CharField(max_length=150)
    
class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    categroy_id = models.ForeignKey(Categroy,on_delete=models.CASCADE)
    
    
