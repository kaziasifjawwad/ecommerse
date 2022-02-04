from rest_framework.serializers import ModelSerializer
from .models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['name','brand','price']