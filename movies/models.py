from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
