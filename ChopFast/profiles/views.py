from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import (CustomerUpdateForm, 
    RiderUpdateForm, 
    StaffUpdateForm)

from app.views import notify

from .models import (Customer, 
    Rider, 
    Supplier, 
    Staff)


@login_required(login_url="/login/")
def profileview(request):

    try:
        rider = Rider.objects.get(user=request.user)
        if rider:
            return redirect(reverse('riderprofile', args=[request.user.id]))
    except Exception as err:
        pass
    try:
        customer = Customer.objects.get(user=request.user)
        if customer:
            return redirect(reverse('customerprofile', args=[request.user.id]))
    except Exception as err:
        pass

    try:
        staff = Staff.objects.get(user=request.user)
        if staff:
            return redirect(reverse('staffprofile', args=[request.user.id]))
    except Exception as err:
        pass


@login_required(login_url='/login/')
def riderprofile(request, id):
    user = User.objects.get(id=id)
    rider = Rider.objects.get(user=user)
    print(rider.id)
    return render(request, 'rider.html', {'rider': rider})


@login_required(login_url='/login/')
def riderUpdateForm(request, riderId):
    r = Rider.objects.get(id=riderId)
    if request.method == "POST":
        riderupdateForm = RiderUpdateForm(request.POST, request.FILES, instance=r)
        if riderupdateForm.is_valid():
            riderupdateForm.save()
            body = f"Hi {r.user.username}, Your Account Update was Successful"
            notify(r.user, body)
    else:
        riderupdateForm = RiderUpdateForm(instance=r)
    return render(request, 'riderProfileUpdate.html', {'form': RiderupdateForm})


@login_required(login_url='/login/')
def staffProfile(request, id):
    user = User.objects.get(id=id)
    staff = Staff.objects.get(user=user)
    print(staff.id)
    return render(request, 'staff.html', {'staff': staff})


@login_required(login_url='/login/')
def staffUpdateForm(request, staffId):
    staff = Staff.objects.get(id=staffId)
    if request.method == "POST":
        staffupdateForm = StaffUpdateForm(request.POST, request.FILES, instance=staff)
        if staffupdateForm.is_valid():
            staffupdateForm.save()
            body = f"Hi {staff.user.username}, Your Account Update was Successful"
            notify(staff.user, body)
    else:
        staffupdateForm = StaffUpdateForm(instance=staff)
    return render(request, 'staffProfileUpdate.html', {'form': staffupdateForm})


@login_required(login_url='/login/')
def customerProfile(request, id):
    user = User.objects.get(id=id)
    customer = Customer.objects.get(user=user)
    return render(request, 'customer.html', {'customer': customer})


@login_required(login_url="/login/")
def customerProfileUpdate(request):
    customer = request.user
    print(customer.customer.id)
    if request.method == "POST":
        customerUpdateForm = CustomerUpdateForm(request.POST, request.FILES, instance=customer)
        if customerUpdateForm.is_valid():
            customerUpdateForm.save()
            body = f"Hi {customer.user.username}, Your Account Update was Successful"
            notify(customer.user, body)
    else:
        customerUpdateForm = CustomerUpdateForm(instance=customer)
    return render(request, "customerProfileUpdate.html", {'form': customerUpdateForm})


# Create your views here.
