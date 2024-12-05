from rest_framework import serializers
from .models import Service, User, Order

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'number', 'email']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['id', 'service', 'user']