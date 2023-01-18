from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product', 'quantity', 'customer')