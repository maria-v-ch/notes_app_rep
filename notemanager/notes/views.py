from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from .models import Note, CustomUser
from .serializers import NoteSerializer, UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


# Template Views
def notes_list(request):
    notes = Note.objects.filter(user=request.user)  # Ensure user is authenticated
    return render(request, 'notes_list.html', {'notes': notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)  # Ensure user is authenticated
    return render(request, 'note_detail.html', {'note': note})
