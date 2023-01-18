from django.db import models
from customer.models import Customer

from order.models import Order

# Create your models here.
class Checkout(models.Model):
    orders = models.ManyToManyField(Order)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)