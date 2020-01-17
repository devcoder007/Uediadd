import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserInfo(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, unique=False)
    last_name = models.CharField(max_length=20, unique=False)
    username = models.CharField(max_length=20, unique=False)
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=40, unique=True)
    user_type = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to = 'pro_pic', default = 'pic_folder/None/no-img.jpg')
    created_at = models.DateTimeField(auto_now_add=True) 
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,
    )

    def __str__(self):
        return self.email
