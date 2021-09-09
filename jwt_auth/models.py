from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    profile_image = models.CharField(max_length=500, blank=True)
    followed_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='following',
        blank=True
    )

    def __str__(self):
        return f'{self.username}'
