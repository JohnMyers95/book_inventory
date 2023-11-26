from django.urls import path

from . import views

app_name = "category"

urlpatterns = [
    path("", views.all, name="all"),
    path("<int:pk>/", views.detail, name="category_detail"),
]
