from operator import truediv
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Education = models.TextField(max_length=100,null=True)
    Area = models.CharField(max_length=100,null=True)
    Email = models.EmailField(max_length=100,null=True)
    Text = models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.Name

class guardian_info(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Class = models.CharField(max_length=100,null=True)
    Subject = models.CharField(max_length=100,null=True)
    Teacher = models.CharField(max_length=100,null=True)
    Area = models.CharField(max_length=100,null=True)
    Email = models.EmailField(max_length=100,null=True)
    Text = models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.Name

