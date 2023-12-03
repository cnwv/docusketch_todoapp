from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserModelSerializer, UserRegisterSerializer


class UsersPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UsersPagination


@api_view(['POST'])
@permission_classes([AllowAny])
def create_auth(request):
    serialized = UserRegisterSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
