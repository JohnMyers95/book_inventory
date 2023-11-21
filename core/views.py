from django.shortcuts import render

from book.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-id")[:8]
    return render(request, "core/index.html", {"books": books})


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
