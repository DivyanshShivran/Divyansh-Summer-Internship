import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expense

@csrf_exempt
def expense_list_api(request):
    """
    Unified API endpoint handling data reads (GET), data writes (POST),
    and record removals (DELETE).
    """
    # --- HANDLE DATA DELETION (DELETE) ---
    if request.method == 'DELETE':
        try:
            payload = json.loads(request.body)
            expense_id = payload.get('id')
            
            if not expense_id:
                return JsonResponse({"error": "Missing expense ID."}, status=400)
                
            # Attempt to find and delete the target record row
            try:
                expense_item = Expense.objects.get(id=expense_id)
                expense_item.delete()
                return JsonResponse({"message": "Expense deleted successfully!"}, status=200)
            except Expense.DoesNotExist:
                return JsonResponse({"error": "Expense record not found."}, status=404)
                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid data format."}, status=400)

    # --- HANDLE DATA WRITING (POST) ---
    elif request.method == 'POST':
        try:
            payload = json.loads(request.body)
            description = payload.get('desc', '').strip()
            amount = payload.get('amount')
            category = payload.get('category')
            
            if not description or amount is None or float(amount) <= 0:
                return JsonResponse({"error": "Invalid form inputs."}, status=400)
                
            new_expense = Expense.objects.create(
                description=description,
                amount=float(amount),
                category=category
            )
            return JsonResponse({"message": "Success", "id": new_expense.id}, status=201)
        except Exception:
            return JsonResponse({"error": "Server error processing entry."}, status=400)

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