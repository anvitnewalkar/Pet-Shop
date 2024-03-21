from django.contrib import admin
from  .models import Product,Category  #it is present in current package so write (.) 
#to import category

# Register your models here.


# admin.ModelAdmin    #it will help to customize interdace

@admin.register(Product) #now tis will work for product module
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','product_description','product_price','product_brand','category')

@admin.register(Category)   #category registered in admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','slug')



# admin.site.register(Product,ProductAdmin) #your product is registered
# Note decorator is working like admin.site

