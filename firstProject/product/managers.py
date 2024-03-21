from django.db import models
from django.db.models.query import QuerySet

class productManager(models.Manager):
    
    # def get_queryset(self):
    #     return super().get_queryset().order_by('product_name')

    # def get_queryset(self):
    #     return super().get_queryset().order_by('product_brand')

    # def get_queryset(self):
    #    return super().get_queryset().filter(product_price__gt = 200)

    def get_queryset(self):
        return productQuerySet(self.model)
    

    def sorted(self):
       return super().get_queryset().order_by('product_name')
    
    def sortByPrice(self):
        return super().get_queryset().order_by('product_price')

class productQuerySet(models.QuerySet):
    
    def getPawsIndia(self):
        return self.filter(product_brand = "Pawsitive")
    
    def dogProducts(self):
        return self.filter(product_name__icontains = "dog")