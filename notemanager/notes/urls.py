from django.urls import path
from . import views

urlpatterns = [
    # API endpoints for users
    path('admin/users/', views.UserList.as_view(), name='user-list'),
    path('admin/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # API endpoints for notes
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    # Template views for notes
    path('', views.notes_list, name='notes_list'),  # List of notes
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),  # Note detail view
]
