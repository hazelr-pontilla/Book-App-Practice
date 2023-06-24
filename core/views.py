from django.shortcuts import render
from store.models import Book

# Create your views here.

def frontpage(request):
    books = Book.objects.all()
    return render(request, 'core/frontpage.html', {'books': books})

def about(request):
    return render(request, 'core/about.html')