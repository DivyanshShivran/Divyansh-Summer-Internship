from django.http import JsonResponse
from django.shortcuts import render
from .models import Expense

def dashboard_view(request):
    """
    Renders and serves the core HTML dashboard template directly 
    from the Django backend template engine layer.
    """
    return render(request, 'index.html')

def expense_list_api(request):
    """
    Fetches all expense logs from the database, extracts their values, 
    and returns a standardized JSON response format.
    """
    expenses_query = Expense.objects.all()
    
    data = []
    for expense in expenses_query:
        # Map fields precisely to align with frontend JavaScript 'item.desc' properties
        data.append({
            "id": expense.id,
            "desc": expense.description,  # Maps backend description to frontend item.desc
            "amount": float(expense.amount),
            "category": expense.category
        })
        
    return JsonResponse({"expenses": data}, safe=False)