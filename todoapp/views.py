# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .models import Category, Task, TaskFile
from .serializers import CategorySerializer, TaskSerializer, TaskFileSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_class =


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_class =

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(data='Task is done', status=status.HTTP_204_NO_CONTENT)


class TaskFileViewSet(RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = TaskFile.objects.all()
    serializer_class = TaskFileSerializer
