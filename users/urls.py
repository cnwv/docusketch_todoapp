from django.urls import re_path
from .views import create_auth

urlpatterns = [
    re_path(r'^users/register/$', create_auth, name='register'),
]
