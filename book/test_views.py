from django.test import TestCase
from book.models import Book


class BookViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            published_date="1997-06-26",
            isbn="9788700631625",
            description="Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.",
            cover_url="https://images-na.ssl-images-amazon.com/images/I/51UoqRAxwEL._SX331_BO1,204,203,200_.jpg",
        )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/books/1", follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get("/books/1", follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp,
            "book/detail.html",
        )


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_books = 13
        for book_id in range(number_of_books):
            Book.objects.create(
                title=f"Harry Potter {book_id}",
                author="JK Rowling",
                published_date="1997-06-26",
                isbn="9788700631625",
                description="Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.",
                cover_url="https://images-na.ssl-images-amazon.com/images/I/51UoqRAxwEL._SX331_BO1,204,203,200_.jpg",
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/books", follow=True)
        self.assertEqual(resp.status_code, 200)
