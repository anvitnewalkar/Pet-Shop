from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q


from.models import Product,Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
@method_decorator(login_required(login_url="/login/"),name = "dispatch")
class ProductView(ListView):
    model = Product
    template_name = "products.html"
    # context['object_list']objectList

class ProductDetailView(DetailView):
    model = Product
    template_name = "Product_detail.html"
    context_object_name = "p"     #It gets by default product

def field_lookup(request):                                  #fuction based view
    #  products = Product.cm.all().getPawsIndia()           #By default manage is objects. It has different methods
    #  products = Product.cm.sortByPrice()
     
    #  products = Product.cm.all().filter(Q(id=7)& Q(product_name__icontains="GoJo"))

    # products = Product.cm.all().filter(Q(product_price__lt="1000")& Q(product_name__icontains="dog"))
    
    # products = Product.cm.all().filter(Q(id=5)| Q(id=7))

    products = Product.pm.all().filter(~Q(product_brand="PawsUp"))

   
    return render(request,"productLookup.html",{"product":products})

    #  products = Product.objects.filter(product_brand = "Pawsitive") #by using filter you get perticular data of your choice

    # products = Product.objects.filter(product_name = "Pet Shampoo")

    # products = Product.objects.filter(product_price__lt = "600")
    
    # products = Product.objects.filter(product_price__lte = "600")

    # products = Product.objects.filter(product_price__gt = "600")

    # products = Product.objects.filter(product_price__gte = "600")

    # products = Product.objects.filter(product_name__contains = "D") #case sensitve 

    # products = Product.objects.filter(product_name__icontains = "Pet")  #case insensitive

    # products = Product.objects.filter(product_brand__startswith = "P") #case sensitive

    # products = Product.objects.filter(product_brand__istartswith = "p") #case insensitive

    # products = Product.objects.filter(product_name__endswith = "s")

    # products = Product.objects.filter(product_name__iendswith = "S")

    # products = Product.objects.filter(id__in = [3,4,5])

    # products = Product.cm.filter(product_price__gt = "400")



class CategoryDetailView(DetailView):
    model = Category
    template_name = "category.html"
    context_object_name = "category"
    slug_field = "slug"

    