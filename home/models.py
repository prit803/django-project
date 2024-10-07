from django.db import models

# Create your models here.
class Student(models.Model): #student is basically scame
    
    # id = models.AutoField() #primary key or automatic django add in scheme
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True , blank = True)
    address = models.TextField(null=True , blank = True)
    

class Product(models.Model):
    pass

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)



    
    def __str__(self) -> str:
        return self.car_name