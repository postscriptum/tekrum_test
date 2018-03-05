from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
    	return self.name


class Purchase(models.Model):
    products = models.ManyToManyField(Product)
    time = models.DateField(auto_now=True)

    def total_price(self):
    	total = 0
    	for product in self.products.all():
    		total += product.price
    	return total

    def get_names(self):
    	return [product.name for product in self.products.all()]
