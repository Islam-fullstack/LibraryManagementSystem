from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet,staff_list

router = DefaultRouter()
router.register('', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', staff_list, name='staff-list'),
]
