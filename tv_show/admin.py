from django.contrib import admin
from . import models

admin.site.register(models.FilmModel)
admin.site.register(models.Review)