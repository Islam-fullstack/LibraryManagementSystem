from django.db import models
from books.models import Book
from members.models import Member


class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews', verbose_name="Kitap")
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='reviews', verbose_name="A'za")
    rating=models.PositiveSmallIntegerField(verbose_name="Baxa (1-5)")
    comment=models.TextField(verbose_name="Kommentariy")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Jaratilgan Waqti")

    def __str__(self):
        return f"{self.member} rated {self.book} ({self.rating/5})"