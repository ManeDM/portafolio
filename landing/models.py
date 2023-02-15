from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class project(models.Model):
    image = ImageField(upload_to='assets/images')
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    url = URLField(blank=True)
