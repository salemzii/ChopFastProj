from django.urls import path
from . import views


urlpatterns = [
    path('updateTask/<int:id>', views.updateTask, name='updateTask'),
    path('addTask', views.addTask, name='addTask')
]
