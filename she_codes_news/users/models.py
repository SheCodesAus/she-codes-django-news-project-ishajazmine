from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User
from django.urls import reverse

class CustomUser(AbstractUser):

    about_me = models.TextField(blank=True)

    image = models.URLField(null = True, blank = True)
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})



# class Post(models.Model):
#         text = models.CharField(max_length=200)
#         posti = models.ImageField(upload_to='media/images', null=True, blank="True")
#         user = models.ForeignKey(User, related_name='imageuser', on_delete=models.CASCADE, default=2)