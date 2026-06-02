# expenses/models.py - Database relational schemas for tracking data

from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - ₹{self.amount}"