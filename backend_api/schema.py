import graphene
from graphene_django import DjangoObjectType

from backend_api.models import Company, Car


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = ("id", "name", "cars")


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("id", "name", "notes", "company")


class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    company_by_name = graphene.Field(CompanyType, name=graphene.String(required=True))

    def resolve_all_cars(root, info):
        return Car.objects.select_related("company").all()

    def resolve_company_by_name(root, info, name):
        try:
            return Company.objects.get(name=name)
        except Company.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)