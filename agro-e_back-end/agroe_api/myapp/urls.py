from django.urls import path
from . import views

urlpatterns = [
    path('trucks/', views.TruckList.as_view(), name='trucks'),
]