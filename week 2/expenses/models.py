from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    """
    Database table schema for the Notes Management System.
    The 'user' field links each note to a specific registered user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE) # <-- This is the owner tag
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=50, default='Personal')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title