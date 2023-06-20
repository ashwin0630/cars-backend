from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('getmain/',views.getmain),
    path('getcar/<str:pk>/',views.getcar),
]
