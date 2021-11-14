from django.shortcuts import render, redirect

from .models import Book, Review

def index(request):
    """The home page for the crazy book club."""
    return render(request, 'crazy_book_club/index.html')

def books(request): 
    """Show all books."""
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'crazy_book_club/books.html', context)

def book(request, book_id):
    """Shows a single book and all its reviews"""
    book = Book.objects.get(id=book_id)
    reviews = book.review_set.order_by('-date_added')
    context = {'book': book, 'reviews': reviews}
    return render(request, 'crazy_book_club/book.html', context)

def reviews(request): 
    """Show all reviews."""
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'crazy_book_club/reviews.html', context)
