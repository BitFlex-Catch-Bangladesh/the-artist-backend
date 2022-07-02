from django.db import models

# Create your models here.
from django.db import models

import uuid


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "the_artist%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Review(models.Model):
    img = models.ImageField(upload_to=generate_filename, null=True)
    title = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    text = models.TextField(null=True)
