from rest_framework.serializers import ModelSerializer

from .models import *


class PackageSerializer(ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
