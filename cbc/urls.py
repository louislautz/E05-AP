"""Defines URL patterns for the crazy_book_club.""" 

from django.urls import path
from . import views

app_name = 'crazy_book_club' 
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Book page
    path('books/', views.books, name='books'),
    # Review page
    path('reviews/', views.reviews, name='reviews'),
    # Detail page for a single book. 
    # path('books/<int:book_id>/', views.book, name='book'),
    # # Page for adding a new topic
    # path('new_book/', views.new_book, name='new_book'),
]