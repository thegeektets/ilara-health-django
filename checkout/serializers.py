from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Checkout
from order.serializers import OrderSerializer

class CheckoutSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Checkout
        fields = ('id', 'orders', 'customer', 'total_price')