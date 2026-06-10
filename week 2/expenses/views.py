import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expense

@csrf_exempt
def expense_list_api(request):
    """
    Unified API endpoint with added server-side validation rules 
    to prevent bad data injection.
    """
    # --- HANDLE DATA WRITING (POST) ---
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            
            description = payload.get('desc', '').strip()
            amount = payload.get('amount')
            category = payload.get('category')
            
            # 1. Check for empty or missing text fields
            if not description:
                return JsonResponse({"error": "Description cannot be empty."}, status=400)
                
            # 2. Check for missing or invalid numeric values
            if amount is None:
                return JsonResponse({"error": "Amount is required."}, status=400)
                
            try:
                amount_value = float(amount)
                # 3. Prevent zero or negative numbers from being processed
                if amount_value <= 0:
                    return JsonResponse({"error": "Amount must be a positive number."}, status=400)
            except ValueError:
                return JsonResponse({"error": "Amount must be a valid number."}, status=400)
                
            # If all checks pass, write safely to SQLite
            new_expense = Expense.objects.create(
                description=description,
                amount=amount_value,
                category=category
            )
            
            return JsonResponse({
                "message": "Expense logged successfully!",
                "id": new_expense.id
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format received."}, status=400)

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