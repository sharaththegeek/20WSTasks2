# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from board.models import User
from board.models import UserProfile
from board.forms import LoginForm
from board.forms import UserDetails

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def register(request):
    return render(request,"register.html",{})

def login(request):
    if request.POST:
        LoginDetails=LoginForm(request.POST)
        if LoginDetails.is_valid():
            email=LoginDetails.cleaned_data['email']
            UPObj=UserProfile.objects.get(email__email=email)
            UPObj.points=UPObj.points+5
            UPObj.save()
            request.session['email']=email
            return HttpResponseRedirect('/rankBoard')
        else:
            return render(request,"home.html",{"message":"Invalid Email or Password","color":"red"})
    else:
        return render(request,"home.html",{"message":"Sorry. We encountered an error!","color":"red"})

def registerUser(request):
    if request.POST:
        UDObj=UserDetails(request.POST)
        if UDObj.is_valid():
            UPObj=UserProfile(firstName=UDObj.cleaned_data['firstName'],lastName=UDObj.cleaned_data['lastName'])
            UPObj.points=0
            UObj=User(email=UDObj.cleaned_data['email'],password=UDObj.cleaned_data['password'])
            UObj.save()
            UPObj.email=UObj
            UPObj.save()
            UObj.save()
            return render(request,"home.html",{"message":"Registered Successfully!","color":"green"})
        else:
            return render(request,"home.html",{"message":"Sorry! Email already exists!","color":"red"})
    else:
       return render(request,"home.html",{})

def logOut(request):
    del request.session['email']
    return render(request,"home.html",{"message":"Logged out successfully!","color":"green"})
       
def rankBoard(request):
    if request.session.has_key('email'):
        cemail=request.session['email']
        UsersTop=UserProfile.objects.all().order_by('-points')[:3]
        UsersOthers=UserProfile.objects.all().order_by('-points')[3:]
        CurrentUser=UserProfile.objects.get(email__email=cemail)
        return render(request,"rankBoard.html",{"UsersTop":UsersTop,"CurrentUser":CurrentUser,"UsersOthers":UsersOthers})
    else:
        return render(request,"home.html",{"message":"Yikes! You have to login first","color":"red"})

def profile(request):
    if request.session.has_key('email'):
        email=request.session['email']
        UPObj=UserProfile.objects.get(email__email=email)
        return render(request,"profile.html",{"UPObj":UPObj})
    else:
        return render(request,"home.html",{})

        