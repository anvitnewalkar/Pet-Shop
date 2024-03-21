from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class Cart(models.Model):          #to inherit models
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    products = models.ManyToManyField(Product,through = "cartItem")

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    products = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

class Order(models.Model):
    order_id = models.CharField(max_length = 200,primary_key = True,default = "OrderXYZ")
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.IntegerField()
    phoneNumber = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    paid = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.firstName}-{self.created_at}"


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    total=models.IntegerField()