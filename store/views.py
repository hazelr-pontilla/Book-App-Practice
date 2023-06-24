from django.shortcuts import render

# Create your views here.
from .models import Book, Category

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    books = category.books.all()
    context = {
        'category': category,
        'books' : books
    }
    return render(request, 'store/category_detail.html', context)

def book_detail(request, category_slug, slug):
    book = Book.objects.get(slug = slug)
    return render(request,  'store/book_detail.html', {'book': book})
