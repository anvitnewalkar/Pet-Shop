from django import template
from datetime import datetime


register = template.Library()   #it will help to register my object
def printDate():
    return datetime.now().strftime("%d-%m-%Y")

register.filter("printDate",printDate)

@register.filter(name = "multiply")
def multiply(v1,v2):
    return v1*v2