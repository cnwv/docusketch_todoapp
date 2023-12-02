from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
# from .filters import ProjectModelFilter, TODOFilter
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework.pagination import LimitOffsetPagination


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
