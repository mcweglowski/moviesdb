from django.contrib import admin

# Register your models here.
from movies.models import Movie, Actor


admin.site.register(Movie)
admin.site.register(Actor)
