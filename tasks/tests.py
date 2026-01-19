from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation_defaults(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "Pending")
        self.assertIsNotNone(task.created_at)

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('task-list-create')

    def test_create_task_success(self):
        data = {'title': 'New Task'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'New Task')

    def test_list_tasks(self):
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task_invalid_status(self):
        data = {'title': 'Bad Task', 'status': 'Invalid'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('status', response.data)
