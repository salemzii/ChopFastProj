from django.urls import path
from . import views


urlpatterns = [
    path('feedbacks', views.feedbacks, name='feedbacksSerializer'),
    path('feedback/<int:feedbackId>', views.feedback, name='feedbackSerializer'),
    path('create-feedback/', views.create_feedback, name='create-feedback'),

    path('reports', views.reports, name='reports'),
    path('report/<int:reportId>', views.report, name='report'),
    path('reportRestaurant', views.reportRestaurant, name='reportRestaurant'),

    path('dishes', views.dishes, name='dishes'),
    path('dishe/<int:dishId>', views.dish, name='dish'),
    path('makedish', views.makedish, name='makedish'),
    path('updatedish/<int:dishId>', views.updatedish, name='updatedish'),

    path('customerprofileupdate/<slug:customerId>', views.customerUpdate, name='customerUpdate'),
    path('customerprofileview/<slug:customerId>', views.customerprofile, name='customerProfile'),

    path('riderprofileupdate/<slug:riderId>', views.riderUpdate, name='riderUpdate'),
    path('riderprofileview/<slug:riderId>', views.riderprofile, name='riderProfile'),

    path('staffprofileupdate/<slug:staffId>', views.staffUpdate, name='staffUpdate'),
    path('staffprofileview/<slug:staffId>', views.staffprofile, name='staffProfile'),
]