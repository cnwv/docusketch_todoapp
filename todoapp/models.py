from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=124)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
