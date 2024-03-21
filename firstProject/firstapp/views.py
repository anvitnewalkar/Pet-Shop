from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.

def home(request):
    return HttpResponse("First view")

def firstpage(request):
    return HttpResponse("<h1>First Page</h1>")

def secondpage(request):
    school = {
              "schoolName":"IES VNS",
              "schoolId":411030,
              "schoolLocation":"Dadar"
              }
    return render(request,"school.html",school)

def users(request):
    student = {"id":101,
               "Name":"Nikita",
               "age":18
    }
    return render(request,"index.html",student)

def register(request):
    return render(request,"register.html")

def submit(request):
    if request.method == "POST":
        return render(request,"submit.html")
    if request.method == "GET":
        return render(request,"register.html")

#class based View
class firstView(View):
    def get(self,request):
        return HttpResponse("class based View - GET")

class secondView(View):
    name = "Nisha"
    def get(self,request):
        return render(request,"detail.html",{"name":self.name}) 
