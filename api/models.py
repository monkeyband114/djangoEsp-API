from pyexpat import model
from django.db import models


# Create your models here.


class Espdata(models.Model):
    name = models.TextField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name[0:40]
    
    
    
    