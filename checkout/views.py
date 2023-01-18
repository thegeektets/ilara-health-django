from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import response, status
from rest_framework.decorators import api_view
from checkout.models import Checkout
from checkout.serializers import CheckoutSerializer
from inventory.models import Product
from inventory.serializers import ProductSerializer
from django.http import JsonResponse

from order.models import Order


# Create your views here.
@api_view(['GET'])
def checkout(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def checkout_detail(request, checkout_id):
    try:
        checkout = Checkout.objects.get(id=checkout_id)
    except Checkout.DoesNotExist:
        return response.Response({'error': 'Checkout not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CheckoutSerializer(checkout)
    return response.Response(serializer.data, status=status.HTTP_200_OK)

def add_order(request, checkout_id):
    checkout = get_object_or_404(Checkout, pk=checkout_id)
    order_form = OrderForm(request.POST or None)

    if order_form.is_valid():
        order = order_form.save(commit=False)
        order.checkout = checkout
        order.save()
        return redirect('checkout_detail', checkout_id=checkout.id)

    return JsonResponse({'status': 'success', 'message': 'Order added successfully'})

def remove_order(request, checkout_id, order_id):
    checkout = get_object_or_404(Checkout, pk=checkout_id)
    order = get_object_or_404(Order, pk=order_id)
    order.delete()

    return JsonResponse({'status': 'success', 'message': 'Order removed successfully'})


def complete_checkout(request, checkout_id):
    checkout = get_object_or_404(Checkout, pk=checkout_id)
    # logic to complete the checkout
    return JsonResponse({'status': 'success', 'message': 'Checkout completed successfully'})

