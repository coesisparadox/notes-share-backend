from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

from .models import User
# Create your views here.
def signup_view(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        faculty=request.POST.get('faculty')
        sem=request.POST.get('sem')
        password=request.POST.get('password')
        print(email,password,sem,faculty)
        user=User.objects.create(email=email,faculty=faculty,sem=sem,password=password)
        user=user.save()
    # print(user)
    return render(request,'accounts/signup.html')


def login_view(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        try:
            user=User.objects.get(email=email,password=password)
            print(user)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully logged in")

            # return redirect('feed_page')
            return HttpResponse("Success")
        except:
        
            messages.error(request,"Invalid")
            return HttpResponse("Invalid")

            # return redirect('feed_page')
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"USer logged out")
    HttpResponse("Success")
    return redirect('feed-page')