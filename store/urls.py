from django.urls import path
from .import views

urlpatterns = [
    path('<slug:slug>/', views.book_detail, name='book-detail'),
    
]
