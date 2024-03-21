from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):            #Inherites its class
    class Meta:                         #class meta tells information about your class
        model = User                             #class name is model/User
        fields = ["username","email","first_name","last_name"] 
        # fields = "__all__"   #alternate methods to get all the methods kind of jugaad  
        labels = {"username":"Enter Username","email":"Email"}  # to  write label of your own choice
        #fields = "__all__"

        