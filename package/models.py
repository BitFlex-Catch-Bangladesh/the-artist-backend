from django.db import models

import uuid


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "the_artist_package%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Package(models.Model):
    choices = [
        ('photos', 'Photos'),
        ('videos', 'Videos'),
        ('combos', 'Combos'),
    ]
    slug = models.SlugField(max_length=200, unique=True, default='')
    category = models.CharField(max_length=10, choices=choices, default='photos')
    img = models.ImageField(upload_to=generate_filename , null=True)
    package_name = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=200, default="100")
    photographer = models.TextField(null=True, blank=True)
    time = models.TextField(null=True, blank=True)
    details = models.JSONField(default=dict, blank=True)
