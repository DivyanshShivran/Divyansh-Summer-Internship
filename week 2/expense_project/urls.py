from django.contrib import admin
from django.urls import path
from expenses.views import dashboard_view, note_list_api 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('api/expenses/', note_list_api, name='notes_api'),
]