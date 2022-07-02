from rest_framework.serializers import ModelSerializer

from .models import *


class HomeBannerSerializer(ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = '__all__'
