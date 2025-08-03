from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Bug(models.Model):
    STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Open")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="bugs")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bugs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
