from rest_framework.serializers import ModelSerializer

from .models import Category, Task, TaskFile


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskFileSerializer(ModelSerializer):
    class Meta:
        model = TaskFile
        fields = '__all__'
        extra_kwargs = {'task': {'required': False}}


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
