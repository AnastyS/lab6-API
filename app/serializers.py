from rest_framework import serializers
from .models import Service, Review, Order

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price',]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'service', 'user', 'rating', 'comment']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['id', 'service', 'customer', 'provider']