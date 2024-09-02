from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Note, CustomUser
from django.contrib.auth import get_user_model


class AdminTests(TestCase):
    def setUp(self):
        # Set up a test client
        self.client = APIClient()

        # Create a test admin user
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass'
        )

        # Create a regular test user
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='userpass'
        )

        # Log in as admin
        self.client.force_authenticate(user=self.admin_user)

    def test_admin_can_list_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_can_create_user(self):
        response = self.client.post(reverse('user-list'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newuserpass'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

    def test_admin_can_retrieve_user(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_admin_can_update_user(self):
        response = self.client.patch(reverse('user-detail', kwargs={'pk': self.user.pk}), {
            'username': 'updateduser'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_admin_can_delete_user(self):
        response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CustomUser.objects.filter(pk=self.user.pk).exists())

    def test_non_admin_cannot_access_admin_routes(self):
        # Log in as a regular user
        self.client.force_authenticate(user=self.user)

        # Attempt to access admin routes
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class NoteTests(TestCase):
    def setUp(self):
        # Set up a test client
        self.client = APIClient()

        # Create a regular test user
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='userpass'
        )

        # Log in as the regular user
        self.client.force_authenticate(user=self.user)

        # Create a test note
        self.note = Note.objects.create(
            title='Test Note',
            description='This is a test note.',
            user=self.user
        )

    def test_user_can_list_notes(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Note')

    def test_user_can_create_note(self):
        response = self.client.post(reverse('note-list'), {
            'title': 'New Note',
            'description': 'This is a new note.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_user_can_retrieve_own_note(self):
        response = self.client.get(reverse('note-detail', kwargs={'pk': self.note.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.note.title)

    def test_user_can_update_own_note(self):
        response = self.client.patch(reverse('note-detail', kwargs={'pk': self.note.pk}), {
            'title': 'Updated Note'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_user_can_delete_own_note(self):
        response = self.client.delete(reverse('note-detail', kwargs={'pk': self.note.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())

    def test_user_cannot_access_other_users_notes(self):
        # Create another user and note
        another_user = get_user_model().objects.create_user(
            username='anotheruser',
            email='anotheruser@example.com',
            password='anotherpass'
        )
        another_note = Note.objects.create(
            title='Another Note',
            description='This is another user\'s note.',
            user=another_user
        )

        # Attempt to access the other user's note
        response = self.client.get(reverse('note-detail', kwargs={'pk': another_note.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


