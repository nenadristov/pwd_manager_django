from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordManager(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.URLField(null=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)