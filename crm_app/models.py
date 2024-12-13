from django.db import models

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# ServiceRequest model
class ServiceRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    assigned_technician = models.ForeignKey('Technician', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

# Technician model
class Technician(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    skills = models.TextField()

    def __str__(self):
        return self.name
