from rest_framework import serializers
from profiles.models import (
    Customer,
    Rider,
    Staff, 
    Supplier
)
from system_supports.models import Feedback, reportRestaurant
from store.models import (
    Dish, 
    Order, 
    OrderItem,
    Delivery,
    Restaurant
)
from django.contrib.auth.models import User



class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['title', 'feedback']


class reportRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = reportRestaurant
        fields = ['customer', 'restaurant', 'report']



class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['dish', 'quantity']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['customer', 'complete']



class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must Match!'})
        user.set_password(password)
        user.save()
        return user



class LoginSerializer(serializers.ModelSerializer):

       class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['image', 'address', 'phone_number']


class RiderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rider
        fields = ['image', 'address', 'phone_number']


class StaffUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ['image', 'address', 'phone_number']

"""
customers
rider
staff
supplier
"""

"""
feedback
reportRestaurant
"""

"""
Dish
Order
Orderitem
Delivery
Restaurant
"""
