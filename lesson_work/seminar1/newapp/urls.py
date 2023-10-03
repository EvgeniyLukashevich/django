from django.urls import path
from . import views

urlpatterns = [
    path('eagle/', views.eagle, name='eagle'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
]
