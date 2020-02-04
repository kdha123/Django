from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Publisher, Author, Book


class AuthorList(ListView):
    model = Author
    # 템플릿파일 : books/author_list.html, 속성object_list


class PublisherList(ListView):
    model = Publisher   # 모든 레코드를 가져오는 경우 클래스명만 지정
    # ListView의 속성object_list
    # 템플릿파일 : 모델명소문자_list.html


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book
    # 특정객체 하나를 가져오는 경우
    # 템플릿파일 : books/모델명소문자_detail.html, 속성object


class AuthorDetail(DetailView):
    model = Author
    # 특정객체 하나를 가져오는 경우
    # 템플릿파일 : books/모델명소문자_detail.html, 속성object


class PublisherDetail(DetailView):
    model = Publisher
    # 특정객체 하나를 가져오는 경우
    # 템플릿파일 : books/모델명소문자_detail.html, 속성object


class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'email', 'intro']
    template_name = 'books/author_insert.html'
    # 속성 form
