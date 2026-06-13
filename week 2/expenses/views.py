import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Note

def dashboard_view(request):
    """Serves the main Notes Management frontend application."""
    return render(request, 'index.html')

@csrf_exempt
def note_list_api(request):
    """
    Unified API handling Notes CRUD operations:
    GET: Fetch all notes
    POST: Save a new note with validation
    DELETE: Remove a note by ID
    """
    if request.method == 'GET':
        notes_query = Note.objects.all().order_by('-created_at')
        data = []
        for note in notes_query:
            data.append({
                "id": note.id,
                "title": note.title,
                "content": note.content,
                "tag": note.tag
            })
        return JsonResponse({"notes": data}, safe=False)

    elif request.method == 'POST':
        try:
            payload = json.loads(request.body)
            title = payload.get('title', '').strip()
            content = payload.get('content', '').strip()
            tag = payload.get('tag', 'General')

            # Backend Validation
            if not title or not content:
                return JsonResponse({"error": "Title and Content fields cannot be empty."}, status=400)

            new_note = Note.objects.create(title=title, content=content, tag=tag)
            return JsonResponse({"message": "Note saved successfully!", "id": new_note.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid format."}, status=400)

    elif request.method == 'DELETE':
        try:
            payload = json.loads(request.body)
            note_id = payload.get('id')
            
            note_item = Note.objects.get(id=note_id)
            note_item.delete()
            return JsonResponse({"message": "Note deleted!"}, status=200)
        except Note.DoesNotExist:
            return JsonResponse({"error": "Note not found."}, status=404)