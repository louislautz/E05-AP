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

def reviews(request): 
    """Show all reviews."""
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'crazy_book_club/reviews.html', context)
