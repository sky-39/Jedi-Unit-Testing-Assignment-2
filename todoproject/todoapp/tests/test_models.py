from django.test import TestCase
from todoapp.models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title='Test Task', description='Test Description', completed=False)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertFalse(self.task.completed)

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')
