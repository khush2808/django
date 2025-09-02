from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    """
    Test the Todo model.
    """
    def test_todo_creation(self):
        todo = Todo.objects.create(title="Test Todo", description="Test description")
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)

class TodoViewTest(TestCase):
    """
    Test the Todo views.
    """
    def setUp(self):
        self.todo = Todo.objects.create(title="Test Todo", description="Test description")

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo:todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo:todo_create'), {
            'title': 'New Todo',
            'description': 'New description',
            'completed': False
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Todo.objects.count(), 2)

    def test_toggle_todo_view(self):
        response = self.client.get(reverse('todo:todo_toggle', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)
