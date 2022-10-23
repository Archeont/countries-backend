from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=256)
    region = models.CharField(max_length=32)
    population = models.IntegerField()
    population_density = models.DecimalField(max_digits=12, decimal_places=2)
    gdp = models.DecimalField(max_digits=20, decimal_places=2)
    gdp_per_capita = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    countries_count = models.IntegerField()
