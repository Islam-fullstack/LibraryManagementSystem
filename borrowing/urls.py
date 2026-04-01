from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowingViewSet, borrowing_list
from . import views

router = DefaultRouter()
router.register('', BorrowingViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('list/', borrowing_list, name='borrowings-list'),
]
