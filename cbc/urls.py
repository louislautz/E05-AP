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
    path('books/<int:book_id>/', views.book, name='book'),
    # Page for adding a new book
    path('new_book/', views.new_book, name='new_book'),
    # Page for adding a new review
    path('new_review/<int:book_id>/', views.new_review, name='new_review'),
    # Page for editing reviews
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]