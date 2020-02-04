from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Publisher, Author, Book


class BookTemplate(TemplateView):
    template_name = 'books/index.html'
    # 템플릿파일에서 사용할 변수를 정의
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['kind'] = ['book', 'author', 'publisher']
        return context


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


class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name', 'address', 'website']
    template_name = 'books/publisher_insert.html'
    success_url = '/books/publisher'
    # 속성 form


class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['name', 'address', 'website']
    template_name = 'books/publisher_update.html'
    success_url = '/books/publisher/{id}/'


class PublisherDelete(DeleteView):
    model = Publisher
    template_name = 'books/publisher_delete.html'
    success_url = '/books/publisher'


class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'email', 'intro', 'photo']
    template_name = 'books/author_insert.html'
    success_url = '/books/author'
    # 속성 form


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'email', 'intro', 'photo']
    template_name = 'books/author_update.html'
    success_url = '/books/author/{id}/'


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'books/author_delete.html'
    success_url = '/books/author'
