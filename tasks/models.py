from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Descripcion', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        row = "Title: " + self.title + " - " +  "Description: " + self.description + " - " +  "User: " + self.user.username
        return row
    
    