import graphene
from graphene_django import DjangoObjectType

from backend_api.models import Company, Car, Sharing
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "sharing")


class SharingType(DjangoObjectType):
    class Meta:
        model = Sharing
        fields = ("id", "user", "car", "created", "updated", "until")


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = ("id", "name", "cars")


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("id", "name", "notes", "company", "sharing")


class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    all_users = graphene.List(UserType)
    all_sharing = graphene.List(SharingType)
    all_companies = graphene.List(CompanyType)
    company_by_name = graphene.Field(CompanyType, name=graphene.String(required=True))

    def resolve_all_sharing(root, info):
        return Sharing.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_companies(root, info):
        return Company.objects.all()

    def resolve_all_cars(root, info):
        return Car.objects.select_related("company").all()

    def resolve_company_by_name(root, info, name):
        try:
            return Company.objects.get(name=name)
        except Company.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)