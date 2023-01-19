from rest_framework import viewsets
from customer.models import Customer
from inventory.models import Product

from order.models import Order, OrderItem
from .models import Checkout
from .serializers import CheckoutSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def create(self, request, *args, **kwargs):
        orders = request.data.get('orders')
        customerId = request.data.get('customer')
        customer = None
        if (customerId):
            customer = Customer.objects.get(id=customerId)

        total_price = request.data.get('total_price')

        checkout = Checkout.objects.create(
            total_price=total_price, customer=customer)
        for order in orders:
            checkout.orders.add(order.get('id'))
            Order.objects.filter(id=order.get('id')).update(status=3)

            orderItems = OrderItem.objects.filter(order=order.get('id'))
            for orderItem in orderItems:
                product = Product.objects.get(id=orderItem.product.id)
                newQuantity = product.quantity-orderItem.quantity
                product.quantity = newQuantity
                product.save()
    
        checkout.save()
        # update the order status for all orders after the create
        return Response(request.data, status=status.HTTP_201_CREATED)
