from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Status(models.Model):
    name = models.CharField(verbose_name="Pavadinimas", max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Pavadinimas", max_length=50)
    price = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    status = models.ForeignKey(to="Status", verbose_name="Būsena", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.customer}, {self.date}, {self.status}"

class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey(to="Product", verbose_name="Prekė", on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(verbose_name="Kiekis")
