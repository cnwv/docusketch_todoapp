import django_filters
from .models import Task, Category


class CategoryModelFilter(django_filters.FilterSet):
    name__contains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name__contains']


class TaskFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__id')
    tag__contains = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
    name__contains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description__contains = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['category', 'tag__contains', 'name__contains', 'description__contains']
