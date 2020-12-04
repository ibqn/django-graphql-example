from django.contrib.auth.models import User
from rest_framework import serializers
from backend_api.models import (
    Car,
    Company,
    Sharing,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = ["url", "name", "cars"]


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ["url", "name", "notes", "company"]


class SharingSerializer(serializers.HyperlinkedModelSerializer):
    # car = serializers.StringRelatedField()
    # user = serializers.StringRelatedField()

    class Meta:
        model = Sharing
        fields = ["url", "car", "user", "created", "updated", "until"]
