from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderItem, OrderStatus
from inventory.serializers import ProductSerializer
from customer.serializers import CustomerSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('id','order', 'product', 'quantity', 'price')

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ('id', 'name')


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer(read_only=True)
    order_items = OrderItemSerializer(
        many=True, read_only=True, source='orderitem_set')
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'price', 'order_items', 'status')
