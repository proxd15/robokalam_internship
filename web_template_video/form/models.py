from django.db import models

# Create your models here.
class form(models.Model):
    name = models.CharField(max_length=50) 
    number = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name
