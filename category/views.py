from django.shortcuts import render, get_object_or_404
from .models import Category
from book.models import Book


# Create your views here.
def detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_books = Book.objects.filter(category=pk)
    featured_books = Book.objects.filter(category=pk)[0:8]
    return render(
        request,
        "category/detail.html",
        {
            "category": category,
            "category_books": category_books,
            "featured_books": featured_books,
        },
    )


def all(request):
    categories = Category.objects.all()
    return render(request, "category/all_categories.html", {"categories": categories})
