from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import BorrowingViewSet, borrowing_list

router = DefaultRouter()
router.register(r'', BorrowingViewSet, basename='borrowing')

urlpatterns = router.urls + [
    path('list/', borrowing_list, name='borrowings-list'),
]