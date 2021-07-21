from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profileview, name='profiles'),
    path('rider/<int:id>', views.riderprofile, name='riderprofile'),
    path('riderUpdate/<slug:riderId>', views.riderUpdateForm, name='riderUpdate'),
    path('customer/<int:id>', views.customerProfile, name='customerprofile'),
    path('customerUpdate', views.customerProfileUpdate, name='customerupdate'),
    path('staff/<int:id>', views.staffProfile, name='staffprofile'),
    path('staff/<slug:staffId>', views.staffUpdateForm, name='staffupdate'),
]
