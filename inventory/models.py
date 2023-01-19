from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.name)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name , self.quantity)
