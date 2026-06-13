from django.db import models

class Note(models.Model):
    """
    Database table schema for the Week 2 Notes Management System project requirement.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=50, default='Personal') # e.g., Work, Study, Personal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title