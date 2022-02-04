from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['favouriteCar','contactInfo','DateOfBirth','email','name','id'][::-1]
        depth = 1