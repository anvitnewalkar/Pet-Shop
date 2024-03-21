from django.contrib.auth.signals import *
# user_logged_in, user user_logged_out, user_login_failed

from django.contrib.auth.models import User
# we will get user

from django.dispatch import receiver
#it is an anotation to recieve the signals

from django.db.models.signals import *
from .models import Product            #importing all product signals values


@receiver(user_logged_in,sender=User)
def log_in(sender,request,user,**kwargs):
    print("****************************")
    print("Logged in successfully")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print("Arguments:",kwargs)
    print("**********************")


@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("*****************************")
    print("Logged out successfully")
    print("Sender:",sender)
    print("request:" , request)
    print("user:, user")
    print("Arguments :" , kwargs)
    print("*******************************")

@receiver(post_save,sender=Product)
def productCreateSignals(sender,instance,**kwargs):
    print("***********Product Created*****************")
    print("********************************************")
    print("sender",sender)
    print("Instance:",instance)
    print("Arguments:",kwargs)
    print("*********************************************")


@receiver(post_delete,sender=Product)
def productCreateSignals(sender,instance,**kwargs):
    print("***********Product Deleted*****************")
    print("********************************************")
    print("sender",sender)
    print("Instance:",instance)
    print("Arguments:",kwargs)
    print("*********************************************")



