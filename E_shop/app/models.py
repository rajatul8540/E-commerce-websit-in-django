from django.db import models
from django.forms import CharField,IntegerField
# Create your models here.
class Categroy(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    categroy_id = models.ForeignKey(Categroy,on_delete=models.CASCADE)
    def __str__(self):
        return self.name,self.categroy_id

class Product(models.Model):
    image = models.ImageField(upload_to='ecommerce/pimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    
