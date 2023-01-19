from rest_framework import viewsets

from inventory.models import Product
from customer.models import Customer

from .models import Order, OrderItem, OrderStatus
from .serializers import OrderSerializer, OrderItemSerializer, OrderStatusSerializer
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data.get('order_items')
        if len(order_data) < 1:
            return Response({'error': 'order items required'}, status=400)
        order_items = []
        customerData = request.data.get('customer')
        if customerData != '' and customerData != None :
            customerId = customerData['id']
            customer = Customer.objects.get(id=customerId)
        else:
            customer = None

        order_status = request.data.get('status')
        price = request.data.get('price')
        order_serializer = self.get_serializer(
            data={'customer': customer, 'order_status': order_status['id'], 'price': price})
        if order_serializer.is_valid():
            order = order_serializer.save()
            order.customer = customer
            order.save()

            for item in order_data:
                productData = item.get('product')
                productId = productData['id']
                product = Product.objects.get(id=productId)
                price = item.get('total')
                quantity = item.get('quantity')
                order_item = OrderItem.objects.create(product=product, quantity = quantity, order = order, price=price)
                order_items.append(order_item)

            headers = self.get_success_headers(order_serializer.data)
            return Response(order_serializer.data, status=200, headers=headers)
        return Response(order_serializer.errors, status=400)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
