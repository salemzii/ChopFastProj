from django.urls import path
from . import views


urlpatterns = [
    path('submit-feedback/', views.create_feedback, name='create-feedback'),
    path('feedback-list/', views.feedback_list, name='feedback_list'),
]
