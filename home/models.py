from django.db import models

# Create your models here.
import uuid


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "the_artist%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class HomeBanner(models.Model):
    image1 = models.ImageField(upload_to=generate_filename, null=True)
    image2 = models.ImageField(upload_to=generate_filename, null=True)
    image3 = models.ImageField(upload_to=generate_filename, null=True)
    image4 = models.ImageField(upload_to=generate_filename, null=True)
