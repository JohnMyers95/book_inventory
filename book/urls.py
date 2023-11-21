from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("", views.all, name="all"),
    path("add/", views.add, name="add"),
    path("search/", views.search, name="search"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/", views.detail, name="detail"),
]
