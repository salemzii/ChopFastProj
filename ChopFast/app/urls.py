# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
#    path('profile', views.profiles),
    path('', views.index, name='home'),
    path('delivery/<int:deliveryId>', views.delivered, name='delivery'),
    # Matches any html file
#+r
#re_path(r'^.*\.*', views.pages, name='pages'),

]
