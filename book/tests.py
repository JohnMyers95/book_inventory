from django.test import TestCase
from book.models import Book


# Create your tests here.
class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            published_date="1997-06-26",
            isbn="9788700631625",
            description="Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.",
            cover_url="https://images-na.ssl-images-amazon.com/images/I/51UoqRAxwEL._SX331_BO1,204,203,200_.jpg",
        )

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_published_date_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("published_date").verbose_name
        self.assertEqual(field_label, "published date")

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("isbn").verbose_name
        self.assertEqual(field_label, "isbn")

    def test_description_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_cover_url_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("cover_url").verbose_name
        self.assertEqual(field_label, "cover url")

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("title").max_length
        self.assertEqual(max_length, 255)

    def test_author_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("author").max_length
        self.assertEqual(max_length, 255)

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("isbn").max_length
        self.assertEqual(max_length, 13)

    def test_cover_url_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("cover_url").max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.title}"
        self.assertEqual(expected_object_name, str(book))
