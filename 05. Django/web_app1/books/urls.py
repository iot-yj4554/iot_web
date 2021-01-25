from django.urls import path
from django.urls.resolvers import URLPattern
from . import views # 현재 패키지 내의 views import

app_name = 'books'

urlpatterns = [
    # /books/
    path('', views.BookModelView.as_view(), name='index'),
    # /books/book/
    path('book/', views.BookList.as_view(), name='book_list'),
    # /books/author/
    path('author/', views.AuthorList.as_view(), name='author_list'),
    # /books/publisher/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
]
