from django.shortcuts import render

# Create your views here.
from .models import Book

def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    return render(request,  'store/book_detail.html', {'book': book})
