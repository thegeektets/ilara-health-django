from django.db import models
from customer.models import Customer
from inventory.models import Product

class OrderStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


