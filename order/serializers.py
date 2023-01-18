from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderItem, OrderStatus

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product', 'quantity', 'customer')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

