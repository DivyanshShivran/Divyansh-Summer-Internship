import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expense

@csrf_exempt
def expense_list_api(request):
    """
    Unified API endpoint to fetch expense records (GET) and 
    process new form submissions to save records (POST).
    """
    # --- HANDLE DATA WRITING (POST) ---
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data stream from the frontend
            payload = json.loads(request.body)
            
            # Extract values precisely matching our database model schema
            description = payload.get('desc')
            amount = payload.get('amount')
            category = payload.get('category')
            
            # Simple server-side sanity check validation
            if not description or not amount:
                return JsonResponse({"error": "Missing mandatory fields."}, status=400)
                
            # Use Django ORM to write a new row directly into the database table
            new_expense = Expense.objects.create(
                description=description,
                amount=float(amount),
                category=category
            )
            
            # Return success status along with the newly created record ID
            return JsonResponse({
                "message": "Expense logged successfully!",
                "id": new_expense.id
            }, status=201)
            
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid data format received."}, status=400)

    # --- HANDLE DATA READING (GET) ---
    elif request.method == 'GET':
        expenses_query = Expense.objects.all()
        
        data = []
        for expense in expenses_query:
            data.append({
                "id": expense.id,
                "desc": expense.description,
                "amount": float(expense.amount),
                "category": expense.category
            })
            
        return JsonResponse({"expenses": data}, safe=False)