from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, StringRelatedField, JSONField, HyperlinkedModelSerializer, \
    SlugRelatedField
from .models import Category, Task, TaskFile


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskFileSerializer(ModelSerializer):
    class Meta:
        model = TaskFile
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    files = TaskFileSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
