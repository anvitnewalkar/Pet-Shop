from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.models import Product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm #to import a readymade form 
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required



def about(request):
    return render(request,"about.html")

def contacts(request):
    return render(request,"contacts.html")

def home(request):
    username = request.session.get("currentUser",None)
    return render(request,"index.html",{"username":username})

@login_required(login_url="/login/")     #to access search page we need to create a decorator
def search(request):
    query = request.GET.get('query','')
    # print(query)
    product = Product.pm.all().filter(product_name__icontains=query)
    return render(request,"search.html",{"AllProducts":product})

def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)           #collecting data from user 
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # form = UserCreationForm()                       #user creation form object is created
        form = RegisterForm()
    return render(request,"register.html",{"form":form})   


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
           #Authrntication
            
            user = authenticate(username = username,password = password)      #calling Authentiucate

            if user is not None:
                login(request,user)  #passing current http request and user object
                request.session["currentUser"] = user.get_username()
                return HttpResponseRedirect("/")

    else:
                form = AuthenticationForm()
    return render(request,"login.html",{"form":form})
    
#user logout function

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")