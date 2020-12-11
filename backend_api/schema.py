import graphene
from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from backend_api.models import Company, Car, Sharing
from django.contrib.auth.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ["id", "username", "email", "sharing"]
        interfaces = (relay.Node,)


class CarNode(DjangoObjectType):
    class Meta:
        model = Car
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
            "notes": ["exact", "icontains"],
            "company": ["exact"],
            "sharing": ["exact"],
        }
        interfaces = (relay.Node,)


class SharingNode(DjangoObjectType):
    class Meta:
        model = Sharing
        filter_fields = {
            "id": ["exact"],
            "user": ["exact"],
            "user__username": ["exact", "icontains", "istartswith"],
            "created": ["exact"],
            "updated": ["exact"],
            "until": ["exact"],
            "car": ["exact"],
            "car__name": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)


class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company
        filter_fields = ["id", "name", "cars"]
        interfaces = (relay.Node,)


class Query(ObjectType):
    car = relay.Node.Field(CarNode)
    all_cars = DjangoFilterConnectionField(CarNode)

    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    sharing = relay.Node.Field(SharingNode)
    all_sharing = DjangoFilterConnectionField(SharingNode)

    company = relay.Node.Field(CompanyNode)
    all_companies = DjangoFilterConnectionField(CompanyNode)


class CreateCompany(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)

    company = graphene.Field(CompanyNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        company = Company.objects.create(name=name)
        return CreateCompany(company=company)


class DeleteCompany(relay.ClientIDMutation):
    class Input:
        id = graphene.String(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        [_, pk] = from_global_id(id)
        company = Company.objects.filter(pk=pk)
        ok = company.exists()
        company.delete()
        return DeleteCompany(ok=ok)


class CreateCar(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        notes = graphene.String(required=True)
        company_id = graphene.String(required=True)

    car = graphene.Field(CarNode)
    company = graphene.Field(CompanyNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, notes, company_id):
        [_, company_pk] = from_global_id(company_id)
        car = Car.objects.create(name=name, notes=notes, company_id=company_pk)
        company = Company.objects.get(pk=company_pk)
        return CreateCar(car=car, company=company)


class Mutation(ObjectType):
    create_company = CreateCompany.Field()
    delete_company = DeleteCompany.Field()

    create_car = CreateCar.Field()


schema = Schema(query=Query, mutation=Mutation)