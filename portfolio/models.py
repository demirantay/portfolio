# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports


class Project(models.Model):
    """
    Data: Project cell data node model
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    header = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(
        upload_to="project_image/", blank=True, null=True
    )
    info = models.CharField(max_length=120, null=True, blank=True)
    link_text = models.CharField(max_length=2000, null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    

    def __str__(self):
        return "Project: " + self.header