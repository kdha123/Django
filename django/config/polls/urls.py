from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), # http://localhost:8000/polls/
    # path('insert/', views.insert), # http://localhost:8000/polls/insert
]
