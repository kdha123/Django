from django.urls import path
from . import views
urlpatterns = [
    # path('url패턴', 수행할 함수 또는 클래스, name=이름)
    path('', views.list),
    path('insert/', views.insert, name='insert')
]
