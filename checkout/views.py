from http.client import ResponseNotReady, responses
from urllib import response
from django.shortcuts import render
from checkout.models import Checkout
from checkout.serializers import CheckoutSerializer

from inventory.serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def checkout(request):
    products = ProductSerializer.objects.all()
    serializer = ProductSerializer(products, many=True)
    return response(serializer.data, status=200)

@api_view(['GET'])
def checkout_detail(request, checkout_id):
    try:
        checkout = Checkout.objects.get(id=checkout_id)
    except Checkout.DoesNotExist:
        return responses({'error': 'Checkout not found'}, status=404)

    serializer = CheckoutSerializer(checkout)
    return ResponseNotReady(serializer.data, status=200)
