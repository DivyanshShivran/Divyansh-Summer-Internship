from django.contrib import admin
from django.urls import path
from expenses.views import expense_list_api, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),  # Serves the HTML frontend on the root URL
    path('api/expenses/', expense_list_api, name='expense-list-api'),  # Backend JSON API
]