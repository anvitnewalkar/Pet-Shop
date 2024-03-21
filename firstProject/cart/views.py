from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,HttpResponse
from product.models import Product
from .models import Cart,CartItem

# Create your views here.

#add to cart button
def add_to_cart(request,productId):

    #logic for adding cart
     
    product = get_object_or_404(Product,id=productId)
    # print(product.product_name)

    # Fetching Current USer
    currentUser = request.user

    cart,created = Cart.objects.get_or_create(user=currentUser)    

    # print(created)

    item,item_created = CartItem.objects.get_or_create(cart = cart,products = product)

    quantity = request.GET.get("quantity")
    
    if not item_created:
        item.quantity += int(quantity)
    else:
        item.quantity = 1
    
    item.save()

    return HttpResponseRedirect("/product/productLookup/")     


    #================================================

    #                 View Cart 

    #=============================================

    #                 Update Cart

    #================================================

def update_cart(request,cartItemId):

    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    quantity=request.GET.get("quantity")
    cartItem.quantity=int(quantity)
    cartItem.save()


    return HttpResponseRedirect("/cart/")

def view_cart(request):
    currentUser = request.user
    cart,created = Cart.objects.get_or_create(user=currentUser)
    cartItems = cart.cartitem_set.all()
    print(cartItems)
    finalAmount = 0

    for item in cartItems:
        finalAmount += item.quantity*item.products.product_price

    return render(request,"cart.html",{"items":cartItems,"finalAmount":finalAmount})



   #===================================================

   #               delete cart

   #===================================================

def delete_cart(request,cartItemId):
    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    cartItem.delete()
    return HttpResponseRedirect("/cart/")                 

   #============================================

   #               Check Out

   #=============================================
from .forms import orderForm
from .models import Order,OrderItem
import uuid                  
def check_out(request):

    currentUser = request.user
    initial = {
         "user":currentUser,
         "firstName":currentUser.get_short_name(),
         "lastName":currentUser.last_name
    }
    form = orderForm(initial= initial)

    currentUser = request.user
    cart,created = Cart.objects.get_or_create(user=currentUser)
    cartItems = cart.cartitem_set.all()
    print(cartItems)
    finalAmount = 0

    for item in cartItems:
        finalAmount += item.quantity*item.products.product_price

    if request.method == "POST":
        form = orderForm(request.POST)
        if form.is_valid():
            user = request.user              #Why to save because to create a new order
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']
            phoneNumber =form.cleaned_data['phoneNumber']

            orderId = str(uuid.uuid4())
            

            order = Order.objects.create(user = user,
                                 firstName = firstName,
                                 lastName = lastName,
                                 address = address,
                                 city = city,
                                 state = state,
                                 pincode = pincode,
                                 phoneNumber = phoneNumber,
                                 order_id = orderId[:8]
                                 )

            for item in cartItems:
                OrderItem.objects.create(

                    order = order,
                    products = item.products,
                    quantity = item.quantity,
                    total = item.quantity*item.products.product_price
                )

        return HttpResponseRedirect("/payment/"+orderId[:8])
    
    return render(request,"checkout.html", {"form":form,"items":cartItems,"finalAmount":finalAmount})


  #============================================

   #               Make Payment

   #=============================================
import razorpay
def make_payment(request,orderId):
    # print(orderId)
    # return HttpResponse("Order added successfully")
  
    order = Order.objects.get(pk=orderId)
    OrderItems = order.orderitem_set.all()
    amount = 0
    for item in OrderItems:
        amount += item.total

    print(amount)
    client = razorpay.Client(auth=("rzp_test_QhUTqq5ri0ueaX", "4JzAfo3vP3akXyEVUF3dneNp"))

    data = { "amount": amount*100, "currency": "INR", "receipt": orderId,"payment_capture":1 }
    payment = client.order.create(data=data)

    return render(request,"payment.html",{"payment": payment})




 #============================================

   #               Payment Successful

   #=============================================

from django.views.decorators.csrf import csrf_exempt    #to import exempt anotation                                          #it will handle by third party ie razorpay
from django.core.mail import send_mail 
@csrf_exempt                                            #it will handle by third party ie razorpay
def success(request,orderId):
    if request.method == "POST":
         client = razorpay.Client(auth=("rzp_test_QhUTqq5ri0ueaX", "4JzAfo3vP3akXyEVUF3dneNp"))
         check = client.utility.verify_payment_signature({
                        'razorpay_order_id': request.POST.get("razorpay_order_id"),
                        'razorpay_payment_id': request.POST.get("razorpay_payment_id"),
                        'razorpay_signature': request.POST.get("razorpay_signature")
                     })
        #  print(check)
         if check:
            order = Order.objects.get(pk=orderId)
            order.paid = True
            order.save()
            cart = Cart.objects.get(user=request.user)
            cart.delete()
            send_mail(
                "Order Placed...",
                "",
                "anvitnwlkrp1@gmail.com",
                ["jari.jafri21@gmail.com","priyanka.vibhute@itvedant.com","roushanshaikh040403@gmail.com"],
                fail_silently = False
            )
            return render(request,"success.html",{})