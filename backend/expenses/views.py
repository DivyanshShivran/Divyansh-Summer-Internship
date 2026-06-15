from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

def dashboard_view(request):
    """Serves the central frontend template dashboard."""
    return render(request, 'index.html')

class NoteViewSet(viewsets.ModelViewSet):
    """
    A secured DRF ViewSet that enforces user isolation.
    Users must be authenticated, and can only interact with their own records.
    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Enforces token requirement

    def get_queryset(self):
        # Override queryset to filter notes belonging strictly to the logged-in user
        return Note.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically attach the authenticated user when a note is saved
        serializer.save(user=self.request.user)