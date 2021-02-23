from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=254)
    mobile = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=254)
    price = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.name


class Menu(models.Model):
    theme = models.CharField(max_length=1,choices=[
        ('B', 'Breakfast'), 
        ('D', 'Diner'), 
        ('F', 'Fast Food')])
    owner = models.ForeignKey(Customer, related_name='menus',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='menus')


    def __str__(self):
        return self.theme