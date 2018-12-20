from django.db import models


class County(models.Model):
    county_name = models.CharField(max_length=200)


class FakeDoctor(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    speciality = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    hospital = models.CharField(max_length=200)


