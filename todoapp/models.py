from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=124)

    def __str__(self):
        return f'{self.name}'


class TaskFile(models.Model):
    file = models.FileField(null=True, upload_to='task_files/')
    uploaded_on = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    tag = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    files = models.ManyToManyField(TaskFile)

    def __str__(self):
        return f'{self.name}'
