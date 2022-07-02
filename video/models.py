from django.db import models


# Create your models here.
class Video(models.Model):
    vid = models.CharField(max_length=250)
