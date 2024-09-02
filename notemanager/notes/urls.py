from django.urls import path
from . import views

urlpatterns = [
    path('admin/users/', views.UserList.as_view(), name='user-list'),
    path('admin/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
]