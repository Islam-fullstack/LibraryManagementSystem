from django.shortcuts import render
from rest_framework import viewsets
from .models import Borrowing
from .serializers import BorrowingSerializer


def borrowing_list(request):
    borrowings = Borrowing.objects.all()
    return render(request, 'borrowing/borrowing_list.html', {'borrowings': borrowings})

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

