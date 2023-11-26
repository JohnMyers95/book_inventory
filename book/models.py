from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    cover_url = models.CharField(max_length=255)
    category = models.ForeignKey(
        "category.Category", on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title
