# Create your models here.
from django.db import models

import uuid


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "the_artist%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Team(models.Model):
    img = models.ImageField(upload_to=generate_filename, null=True)
    name = models.CharField(max_length=500, null=True)
    designation = models.CharField(max_length=500, null=True)

