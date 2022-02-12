from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username



# class Post(models.Model):
#         text = models.CharField(max_length=200)
#         posti = models.ImageField(upload_to='media/images', null=True, blank="True")
#         user = models.ForeignKey(User, related_name='imageuser', on_delete=models.CASCADE, default=2)