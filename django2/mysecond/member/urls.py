from django.urls import path
from . import views
urlpatterns = [
    # path('url패턴', 수행할 함수 또는 클래스, name=이름)
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('insert/', views.insert, name='insert'),
    # int형의 변수 memeber_id로 간다.
    path('<int:member_id>/', views.detail, name='detail')
]
