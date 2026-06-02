from django.contrib import admin
from django.urls import path
from expenses.views import expense_list_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/expenses/', expense_list_api, name='expense-list-api'),
]