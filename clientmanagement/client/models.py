

from django.db import models


# Create your models here.

class Industry(models.Model):
   name = models.CharField(max_length = 150 , null=True)
   
   def __str__(self):
       return self.name
   

class Client(models.Model):
    name= models.CharField(max_length=150, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class ServicesCategory(models.Model):
    name=models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name= models.CharField(max_length = 150)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    date_started = models.DateField(auto_now=False, auto_now_add=False)
    date_ended = models.DateField(auto_now=False, auto_now_add=False)
    Price = models.FloatField()
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    
