# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from profiles.models import Customer, Rider, Staff, Supplier
import time

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from coreapis.serializers import RegistrationSerializer, LoginSerializer


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        t1 = time.time()

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                t2 = time.time()
                print(f"Total login time taken {t2 - t1}")
                return redirect("restaurant")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            u = User.objects.get(username=username)
            u.is_active = True
            u.save()

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            token = Token.objects.create(user=u)
            token.save()

            customer = Customer.objects.create(
                user=u,
                address='Middle Street kano'
            )
            customer.save()
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })



def register_staff(request):
    
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        staff_type = request.POST['choice']
        if form.is_valid():
            t1 = time.time()
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            u = User.objects.get(username=username)
            u.is_active = True
            u.save()
            token = Token.objects.create(user=u)
            token.save()

            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            if staff_type == "rider":
                rider = Rider.objects.create(
                    user=u,
                    address="middle street kano"
                )
                rider.user.is_staff = True
                rider.save()
            elif staff_type == 'staff':
                staff = Staff.objects.create(
                    user=u,
                    address="middle street kano"
                )
                staff.user.is_staff = True
                staff.save()
            elif staff_type == 'supplier':
                supplier = Supplier.objects.create(
                    user=u,
                    address="middle street kano"
                )
                supplier.save()
            else:
                msg = f'Please specify a role for {u.username}'
                success = False
            t2 = time.time()
            print(f"Total time taken {t1 - t2}")
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/registerStaff.html", {"form": form, "msg" : msg, "success" : success })


@api_view(['POST'])
def registrationView(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Sucessfully Created Your Account!'
            data['email'] = user.email
            data['username'] = user.username
            user.is_active = True
            user.save()
            token = Token.objects.create(user=user)
            token.save()
        else:
            data = serializer.errors
        return Response(data)

