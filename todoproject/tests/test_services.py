from django.test import TestCase
from todoapp.services import TaskService
from todoapp.models import Task

class TaskServiceTest(TestCase):

    def setUp(self):
        self.task = TaskService.create_task('Test Task', 'Test Description', False)

    def test_create_task(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertFalse(self.task.completed)

    def test_get_task(self):
        task = TaskService.get_task(self.task.pk)
        self.assertEqual(task, self.task)

    def test_update_task(self):
        updated_task = TaskService.update_task(self.task, 'Updated Task', 'Updated Description', True)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.description, 'Updated Description')
        self.assertTrue(updated_task.completed)

    def test_delete_task(self):
        TaskService.delete_task(self.task)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task.pk)
