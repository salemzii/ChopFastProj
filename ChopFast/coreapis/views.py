from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, 
    IsAuthenticated, 
    IsAdminUser)
from system_supports.models import (Feedback,
 reportRestaurant)
from store.models import (Dish, 
    Delivery, Restaurant, 
    Customer, Payments, 
    Order, OrderItem)
from .serializers import (FeedbackSerializer, 
    DishSerializer,
    reportRestaurantSerializer,
    CustomerUpdateSerializer,
    RiderUpdateSerializer,
    StaffUpdateSerializer,
    UserViewSerializer)

from profiles.models import (Staff,
    Rider,
    Customer)
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def feedbacks(request):
    feedbacks = Feedback.objects.all()
    serializer = FeedbackSerializer(feedbacks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def feedback(request, feedbackId):
    feedback = Feedback.objects.get(id=feedbackId)
    serializer = FeedbackSerializer(feedback, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_feedback(request):
    feedbackSerializer = FeedbackSerializer(data=request.data)
    if feedbackSerializer.is_valid():
        feedbackSerializer.save()
    return Response(feedbackSerializer.data)


@api_view(['GET'])
def reports(request):
    reports = reportRestaurant.objects.all()
    serializer = reportRestaurantSerializer(reports, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def report(request, reportId):
    try:
        report = reportRestaurant.objects.get(id= reportId)
    except Exception as err:
        return redirect('reports')
    serializer = reportRestaurantSerializer(report, many=True)
    return Response(serializer.data)  


@api_view(['POST'])
def reportRestaurant(request):
    reportSerializer = reportRestaurantSerializer(request.data)
    print(dir(reportSerializer))
    reportSerializer.instance.customer_id = request.user.id
    if reportSerializer.is_valid():
        reportSerializer.save()
    return Response(reportSerializer.data)


@api_view(['POST'])
def makedish(request):
    dishSerializer = DishSerializer(data=request.data)
    if dishSerializer.is_valid():
        dishSerializer.save()
    return Response(dishSerializer.data)


@api_view(['POST'])
def updatedish(request, dishId):
    dish = Dish.objects.get(id=dishId)
    serializer = DishSerializer(data=request.data, instance=dish)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def dishes(request):
    dishes = Dish.objects.all()
    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dish(request, dishId):
    dish = Dish.objects.get(id = dishId)
    serializer = DishSerializer(dish, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def customerprofile(request, customerId):
    customer = Customer.objects.get(id=customerId)
    user = User.objects.get(customer=customer)
    serializer = CustomerUpdateSerializer(customer, many=False)
    serialer2 = UserViewSerializer(user, many=False)
    data = {}
    data['username'] = serialer2.data['username']
    data['email'] = serialer2.data['email']
    data['image'] = serializer.data['image']
    data['address'] = serializer.data['address']
    data['phone_number'] = serializer.data['phone_number']
    return Response(data)


@api_view(['GET'])
def riderprofile(request, riderId):
    rider = Rider.objects.get(id=riderId)
    user = User.objects.get(rider=rider)
    serializer = RiderUpdateSerializer(rider, many=False)
    serialer2 = UserViewSerializer(user, many=False)
    data = {}
    data['username'] = serialer2.data['username']
    data['email'] = serialer2.data['email']
    data['image'] = serializer.data['image']
    data['address'] = serializer.data['address']
    data['phone_number'] = serializer.data['phone_number']
    return Response(data)


@api_view(['GET'])
def staffprofile(request, staffId):
    staff = Staff.objects.get(id=staffId)
    user = User.objects.get(staff=staff)
    serializer = StaffUpdateSerializer(staff, many=False)
    serialer2 = UserViewSerializer(user, many=False)
    data = {}
    data['username'] = serialer2.data['username']
    data['email'] = serialer2.data['email']
    data['image'] = serializer.data['image']
    data['address'] = serializer.data['address']
    data['phone_number'] = serializer.data['phone_number']
    return Response(data)


@api_view(['PUT'])
def customerUpdate(request, customerId):
    customer = Customer.objects.get(id=customerId)
    serializer = CustomerUpdateSerializer(data=request.data, instance=customer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def riderUpdate(request, riderId):
    rider = Rider.objects.get(id=riderId)
    serializer = RiderUpdateSerializer(data=request.data, instance=rider)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def staffUpdate(request, staffId):
    staff = Staff.objects.get(id=staffId)
    serializer = StaffUpdateSerializer(data=request.data, instance=staff)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
