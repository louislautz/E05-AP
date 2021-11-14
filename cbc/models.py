from django.db import models
from django.db.models.fields.json import JSONField
from django.contrib.auth.models import User


class Book(models.Model):
    """Describes a book class"""
    name = models.CharField(max_length=150) #limits the length of the name
    authors = models.JSONField()
    year_published = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True) #automatically sets field when first created
    date_modified = models.DateTimeField(auto_now=True) #automatically sets field each time its saved
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a message that describes the book"""
        return f"{self.name} by {self.authors}, published in {self.year_published}"


class Review(models.Model):
    """Describes the Review class"""
    text = models.TextField()
    stars = models.IntegerField()
    unfinished = models.BooleanField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True) #automatically sets field when first created
    date_modified = models.DateTimeField(auto_now=True) #automatically sets field each time its saved

    def __str__(self):
        """Return a string representation of the review"""
        return f"{self.text[:50]}..."
