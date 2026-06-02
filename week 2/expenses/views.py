from django.http import JsonResponse

def expense_list_api(request):
    mock_data = [
        {"id": 1, "description": "Lunch at cafeteria", "amount": 250.00, "category": "Food"},
        {"id": 2, "description": "Monthly travel pass", "amount": 1200.00, "category": "Transport"},
        {"id": 3, "description": "Internet Bill", "amount": 799.00, "category": "Bills"}
    ]
    return JsonResponse(mock_data, safe=False)