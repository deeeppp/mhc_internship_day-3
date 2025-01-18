from django.contrib import admin 
from .models import Electronics,Fashion,Grocery 
@admin.register(Electronics) 
class ElectronicsAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'color', 'brand') 

@admin.register(Fashion) 
class FashionAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'color', 'brand') 

@admin.register(Grocery) 
class GroceryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'quantity') 

 