from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    company = models.ForeignKey(Company, related_name="cars", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sharing(models.Model):
    user = models.ForeignKey(
        "auth.User", related_name="sharing", on_delete=models.CASCADE
    )
    car = models.ForeignKey(Car, related_name="sharing", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    until = models.DateTimeField()