from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import BookForm
from django.db.models import Q


# Create your views here.
def detail(request, pk):
    if request.method == "DELETE":
        delete(request, pk)
    else:
        book = get_object_or_404(Book, pk=pk)
        authors_other_books = Book.objects.filter(author=book.author).exclude(pk=pk)[
            0:3
        ]
        same_category_books = Book.objects.filter(category=book.category)[0:3]
        return render(
            request,
            "book/detail.html",
            {
                "book": book,
                "authors_other_books": authors_other_books,
                "same_category_books": same_category_books,
            },
        )


def all(request):
    books = Book.objects.all()
    return render(request, "book/all_books.html", {"books": books})


def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book:all")
    else:
        form = BookForm()
    return render(request, "book/add.html", {"form": form})


def delete(request, pk):
    if request.method == "DELETE":
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect("book/all_books.html")


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book:all")
    else:
        form = BookForm(instance=book)
    return render(request, "book/edit.html", {"form": form, "pk": pk})


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "DELETE":
        book.delete()
        return redirect("book:all")
    return render(request, "book/delete.html", {"book": book, "pk": pk})


def search(request):
    search_query = request.GET.get("q", "")
    books = Book.objects.filter(
        Q(title__contains=search_query) | Q(author__contains=search_query)
    )
    return render(request, "book/search.html", {"books": books})
