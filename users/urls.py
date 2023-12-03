from django.urls import path

from .views import create_auth

urlpatterns = [
    path('register/', create_auth, name='register'),
]
