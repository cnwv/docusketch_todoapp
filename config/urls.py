from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from todoapp.views import CategoryViewSet, TaskFileViewSet, TaskViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('categories', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login', obtain_auth_token),
    path('api/auth/', include('users.urls')),
    path(
        'api/tasks/<int:task_id>/task_files/',
        TaskFileViewSet.as_view({'post': 'create'}),
        name='files-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
