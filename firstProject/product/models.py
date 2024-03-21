from django.db import models

from .managers import productManager

from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
     category_name = models.CharField(max_length = 12)
     slug = AutoSlugField(populate_from = "category_name")

     def __str__(self):
          return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_description = models.TextField(default = "description")
    product_price = models.IntegerField(default = 0)
    product_brand = models.CharField(max_length = 100,default = "Paws")
    product_picture = models.ImageField(upload_to = "images/",default = "")
#   category = models.ForeignKey(Category,on_delete = models.CASCADE,null=True)
#   category = models.ForeignKey(Category,on_delete = models.PROTECT,null=True)
    category = models.ForeignKey(Category,on_delete = models.SET_NULL,null=True)


    pm = models.Manager()
    cm = productManager()

    def __str__(self):
         return self.product_name

    #def __str__(self):
        #return self.product_brand
