from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), # http://localhost:8000/polls/
    path('test/', views.test), # http://localhost:8000/polls/test/
    path('insert/', views.insert), # http://localhost:8000/polls/insert
    path('list/', views.list), # http://localhost:8000/polls/list
]
