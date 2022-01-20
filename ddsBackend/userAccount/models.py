from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.

# Extended the user base model to store the information of all kind of user of the app.
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_no = models.IntegerField(null=True)
    total_upload = models.IntegerField(null=True)
    user_avatar = models.ImageField(null=True, blank=True, upload_to="images/avatar")
    role_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
