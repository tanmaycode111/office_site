from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_role =models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} .  Job Role : {self.job_role}\n Email : {self.email}. \n Gender : {self.gender}. \n Address : {self.address}."