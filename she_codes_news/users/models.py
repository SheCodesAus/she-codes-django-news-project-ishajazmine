from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) 
#     # ^above should delete the user profile when user is deleted
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'

# error returned: 
# ImportError: Module 'users.apps' does not contain a 'Profile' class. Choices are: 'UsersConfig'.
