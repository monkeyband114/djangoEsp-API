from tkinter import E
from rest_framework.serializers import ModelSerializer
from .models import Espdata


class EspSerializer(ModelSerializer):
    class Meta:
        model = Espdata
        fields = '__all__'
    