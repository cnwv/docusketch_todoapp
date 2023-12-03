from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .filters import CategoryModelFilter, TaskFilter
from .models import Category, Task, TaskFile
from .serializers import CategorySerializer, TaskFileSerializer, TaskSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryModelFilter


class TaskViewSet(RetrieveModelMixin,
                  ListModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin,
                  GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(data='Task is done', status=status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['task_id'] = self.kwargs.get('pk', None)
        return context

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        files_serializer = TaskFileSerializer(
            instance.taskfile_set.all(), many=True)
        response_data = {
            'task': serializer.data,
            'files': files_serializer.data
        }
        return Response(response_data)


class TaskFileViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = TaskFileSerializer

    def perform_create(self, serializer):
        task_id = self.kwargs.get('task_id')
        serializer.save(task_id=task_id)

    def get_queryset(self):
        return TaskFile.objects.filter(task_id=self.kwargs['task_id'])
