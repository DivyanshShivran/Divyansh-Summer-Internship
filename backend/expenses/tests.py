from django.test import TestCase
from .models import Expense

class ExpenseModelBasicTest(TestCase):
    def test_expense_structure(self):
        """Verify that our app can read fields from the models blueprint."""
        # This checks that our defined structure doesn't throw syntax errors
        self.assertTrue(hasattr(Expense, 'description'))
        self.assertTrue(hasattr(Expense, 'amount'))
        self.assertTrue(hasattr(Expense, 'category'))