from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
