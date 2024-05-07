from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField(null=True, blank=True) 
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    user_avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar/', default='default-avatar.png')
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # display user with full name in the database
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.user_avatar.url
        except:
            url = '/images/default-avatar.png'
        return url