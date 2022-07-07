from django.db import models


# Create your models here.
class Contact(models.Model):
    bf_name = models.CharField(max_length=250, null=True)
    bl_name = models.CharField(max_length=250, null=True)
    gf_name = models.CharField(max_length=250, null=True)
    gl_name = models.CharField(max_length=250, null=True)
    wedding_dates =  models.CharField(max_length=250, null=True)
    event_details = models.TextField()
    venue = models.TextField()
    c_number = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    story = models.TextField()
    thoughts = models.TextField()
