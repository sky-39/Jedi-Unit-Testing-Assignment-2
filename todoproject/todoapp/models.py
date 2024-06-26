from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title