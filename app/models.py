#from django.db import models

# Create your models here.
from unittest.util import _MAX_LENGTH
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    

    def __str__(self):
        return self.username
