from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from books.models import Book, Author, Publisher

# Create your views here.

# TemplateView
class BookModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

# ListView
# 아래 두줄의 코드는 내부적으로 자동 생성됨
# object_list = self.model.objects.all() # model --> Book
# context['object_list'] = object_list

# 템플릿 명 규칙 : 모델명(소문자)_list.html # book_list.html
# 내부적으로 url을 지정해주기 때문에 따로 지정하지 않아도 됨
# 내가 원하는 이름으로 바꾸고 싶으면 바꿀 수 있음 # template_name = 'books/book_mylist.html' 

class BookList(ListView):
    model = Book
class AuthorList(ListView):
    model = Author
class PublisherList(ListView):
    model = Publisher

# DetailView
class BookDetail(DetailView):
    model = Book
class AuthorDetail(DetailView):
    model = Author
class PublisherDetail(DetailView):
    model = Publisher