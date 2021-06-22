from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField(default=0000000000)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.username
