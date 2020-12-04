from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from rest_framework import routers
from rest_api import views

from rest_api.views import (
    CarViewSet,
    CompanyViewSet,
    UserViewSet,
    SharingViewSet,
)


router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("cars", views.CarViewSet)
router.register("companies", views.CompanyViewSet)
router.register("sharing", views.SharingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
