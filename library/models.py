from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateTimeField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    tittle = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    edition_date = models.DateTimeField()

class Condition(models.Model):
    condition = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    avaible = models.BooleanField()
    