from rest_framework.serializers import ModelSerializer
from .models import Category, Task


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
