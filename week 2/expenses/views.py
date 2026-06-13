from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

def dashboard_view(request):
    """Serves the central frontend template dashboard."""
    return render(request, 'index.html')

class NoteViewSet(viewsets.ModelViewSet):
    """
    A professional DRF ViewSet that replaces manual view handling.
    Automatically provides complete GET, POST, PUT, and DELETE API endpoints.
    """
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer