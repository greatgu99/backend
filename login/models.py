from django.db import models

# Create your models here.
class User(models.Model):
    UserAccount = models.CharField(max_length=200)
    UserPassword = models.CharField(max_length=200)
    def __str__(self):
        return self.UserAccount