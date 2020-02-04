from django.urls import path
from . import views
from .models import Publisher
# 클래스형 뷰
app_name = 'books'
urlpatterns = [
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    path('author/', views.AuthorList.as_view(), name='author_list'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
    path('author/insert/', views.AuthorCreate.as_view(), name="author_insert"),
]

# 진입메소드: as_view(), urls.py에서 as_view()를 호출하여 실행
