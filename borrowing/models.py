from django.db import models
from books.models import Book
from members.models import Member
from datetime import datetime, date

class Borrowing(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowing', verbose_name="Kitap")
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='borrowing', verbose_name="A'za")
    borrow_date=models.DateField(auto_now_add=True, verbose_name="Ijaraga alghan kuni")
    return_date=models.DateField(null=True,blank=True, verbose_name="Qaytarghan kuni")
    due_date = models.DateField(null=True, blank=True, verbose_name="Qaytariliwi kerek bolghan kuni")

    def is_overdue(self):
        if self.return_date is None and date.today() > self.due_date:
            return True
        return False
    
    def __str__(self):
        return f"{self.member} borrowed {self.book}"
    

