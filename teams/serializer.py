from rest_framework.serializers import ModelSerializer

from .models import *


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
