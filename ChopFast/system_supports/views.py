from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Create_feedback, reportRestaurantForm
from .models import Feedback, reportRestaurant
from store.models import Restaurant
from profiles.models import Customer
from django.contrib.auth.models import User


def create_feedback(request):
    if request.method == "POST":
        feedback = Create_feedback(request.POST)
        if feedback.is_valid():
            feedback.save()
            return redirect('feedback_list')
    else:
        feedback = Create_feedback()
    return render(request, 'addFeedback.html', {'form': feedback})


def feedback_list(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'feedbacks.html', {'feedbacks': feedback_list})


def report_Restaurant(request, id):
    customer = Customer.objects.get(user=request.user)
    restaurant = Restaurant.objects.get(id=id)
    if request.method == "POST":
        reportForm = reportRestaurantForm(request.POST)
        if reportForm.is_valid():
            reportForm.instance.customer_id = customer.id
            reportForm.instance.restaurant_id = restaurant.id
            reportForm.save()
            return redirect('feedback_list')
    else:
        reportForm = reportRestaurantForm()
    return render(request, 'userauth/reportDoc.html', {'reportform': reportForm})


# Create your views here.
