from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.

class auth_user(models.Model):
    id = models.IntegerField()
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)