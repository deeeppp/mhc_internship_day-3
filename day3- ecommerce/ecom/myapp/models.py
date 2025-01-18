from django.db import models 

class Electronics(models.Model): 
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

def __str__(self): 
    return f"{self.name} {self.price}" 

class Fashion(models.Model): 
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

def __str__(self): 
    return f"{self.name} {self.price}" 

class Grocery(models.Model): 
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    

def __str__(self): 
    return f"{self.name} {self.price}" 