from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from todoapp.views import TaskViewSet, CategoryViewSet, TaskFileViewSet
from users.views import UserViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('categories', CategoryViewSet)
router.register('task_files', TaskFileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)