from django.http import JsonResponse
from .models import Expense

def expense_list_api(request):
    """
    Fetches all expense logs from the database, extracts their values, 
    and returns a standardized JSON response format.
    """
    # Fetch all records safely using the Django ORM
    expenses_query = Expense.objects.all()
    
    # Serialize database table records into a clean python dictionary array
    data = []
    for expense in expenses_query:
        data.append({
            "id": expense.id,
            "description": expense.description,
            "amount": float(expense.amount),  # Enforce basic numeric float data type
            "category": expense.category
        })
        
    # Return data matrix safely across the application connection layer
    return JsonResponse({"expenses": data}, safe=False)