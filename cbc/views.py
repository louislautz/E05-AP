from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Book, Review
from .forms import BookForm, ReviewForm

def index(request):
    """The home page for the crazy book club."""
    return render(request, 'crazy_book_club/index.html')

@login_required
def books(request): 
    """Show all books."""
    books = Book.objects.filter(owner=request.user).order_by('date_added')
    context = {'books': books}
    return render(request, 'crazy_book_club/books.html', context)

@login_required
def book(request, book_id):
    """Shows a single book and all its reviews"""
    book = Book.objects.get(id=book_id)
    
    # Make sure the book belongs to the current user.
    if book.owner != request.user:
        raise Http404

    reviews = book.review_set.order_by('-date_added')
    context = {'book': book, 'reviews': reviews}
    return render(request, 'crazy_book_club/book.html', context)

@login_required
def new_book(request):
    """Add a new book."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BookForm()
    else:
        # POST data submitted; process data.
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()
            return redirect('crazy_book_club:books')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'crazy_book_club/new_book.html', context)

@login_required
def reviews(request): 
    """Show all reviews."""
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'crazy_book_club/reviews.html', context)

@login_required
def new_review(request, book_id):
    """Adds a new review to a particular book"""
    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ReviewForm()
    else:
        # POST data submitted; process data.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.save()
            return redirect('crazy_book_club:reviews') # TODO change to book with specific book ID

    # Displays a blank or invalid form.
    context = {'book': book, 'form': form}
    return render(request, 'crazy_book_club/new_review.html', context)

@login_required
def edit_review(request, review_id):
    """Changes an existing review"""
    review = Review.objects.get(id=review_id)
    book = review.book
    if book.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request; pre-fill form with the current directory
        form = ReviewForm(instance=review)
    else:
        # POST data submitted; process data.
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('crazy_book_club:book', book_id=book.id)
    
    context = {'review': review, 'book': book, 'form': form}
    return render(request, 'crazy_book_club/edit_review.html', context)
