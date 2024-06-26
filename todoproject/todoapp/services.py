from .models import Task

class TaskService:

    @staticmethod
    def create_task(title, description, completed):
        return Task.objects.create(title=title, description=description, completed=completed)

    @staticmethod
    def get_task(pk):
        return Task.objects.get(pk=pk)

    @staticmethod
    def update_task(task, title, description, completed):
        task.title = title
        task.description = description
        task.completed = completed
        task.save()
        return task

    @staticmethod
    def delete_task(task):
        task.delete()
