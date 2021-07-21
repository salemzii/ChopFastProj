# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, register_staff, registrationView
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('registerstaff/', register_staff, name="registerStaff"),
    path('google/', TemplateView.as_view(template_name="gauth.html"), name="google"),
    path("logout/", LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('registrationapiView/', registrationView, name='regitrationApiView')
]

