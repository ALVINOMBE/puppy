from django.db import models

# Create your models here.
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Breed(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Dog(models.Model):
    name = models.CharField(max_length=255)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True, blank=True)

class HealthRecord(models.Model):
    summary = models.CharField(max_length=255)
    details = models.TextField()
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey('Veterinarian', on_delete=models.SET_NULL, null=True, blank=True)

class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Veterinarian(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
