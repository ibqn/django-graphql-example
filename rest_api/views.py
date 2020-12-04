from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_api.serializers import (
    UserSerializer,
    CarSerializer,
    CompanySerializer,
    SharingSerializer,
)
from backend_api.models import Car, Company, Sharing


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SharingViewSet(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]