from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib import messages
# Create your views here.
def signout(request):
    
    logout(request)
    return redirect('home')


def show_account(request):
    context={}
    if request.method == "POST" and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create a user account 
            user =User.objects.create_user(username=username,
                                    password=password,
                                    email=email,)
            #create customer 
            Customer.objects.create(user=user,
                                    name=username,
                                    address=address,
                                    phone=phone)
            
            succsess = "Registration successful!"
            messages.success(request,succsess,extra_tags='success')
            return redirect('home')
            
       
        except Exception as e:
           errorss = "Duplicate user name or invalid input"
           messages.error(request,errorss, extra_tags='register')

    if request.method=="POST" and 'login' in request.POST:
        context['register']=False
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')

            user= authenticate(request,username=username,password=password)

            if user:
                login(request,user)
                succsess = "Login successful!"
                messages.success(request,succsess,extra_tags='lsuccess')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password", extra_tags='login')

        except Exception as e:
            errorss = " invalid credentials"
            messages.error(request,errorss, extra_tags='login')

             
           
    return render(request,'account.html',context)