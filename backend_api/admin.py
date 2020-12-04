from django.contrib import admin

from backend_api.models import (
    Company,
    Car,
)

admin.site.register(Company)
admin.site.register(Car)