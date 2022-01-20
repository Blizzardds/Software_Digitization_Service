from django.db import models
from userAccount.models import User


# Create your models here.

# File model to store files info and meta data into the database.
class myFile(models.Model):
    index = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    doc = models.FileField(upload_to="media/documents/", null=False)
    uploader = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateTimeField(auto_now_add=True, null=False)
    modified_date = models.DateTimeField(auto_now=True, blank=True)
    expiary_date = models.DateTimeField(blank=True)
    is_lock = models.BooleanField(default=False, blank=True, null=True)
    group_id = models.ForeignKey
    is_private = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.title


# Archived Files model to store the archived files info and meta data into the database.
class ArchivedFile(models.Model):
    index = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    doc = models.FileField(upload_to="archived_doc/", null=False)
    uploader = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateTimeField(auto_now_add=True, null=False)
    expiary_date = models.DateTimeField(blank=True)
    group_id = models.ForeignKey
    is_private = models.BooleanField(default=False, blank=False)
    archive_date = models.DateTimeField(auto_now_add=True, null=False)

    def str(self):
        return self.title
