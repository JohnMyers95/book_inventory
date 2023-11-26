from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
