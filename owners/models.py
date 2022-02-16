from tkinter import CASCADE
from django.db import models

class Opener(models.Model):
    name  = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age   = models.IntegerField()
    class Meta:
        db_table= 'openers'
            
class Cat(models.Model):
    name   = models.CharField(max_length=45)
    age    = models.IntegerField()
    opener = models.ForeignKey('Opener', on_delete=models.CASCADE)
    class Meta:
        db_table= 'cats'