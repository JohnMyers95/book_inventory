from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("books/", include("book.urls")),
    path("categories/", include("category.urls")),
    path("admin/", admin.site.urls),
]
