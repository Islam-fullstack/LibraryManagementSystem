from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ReviewViewSet, review_list

router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='review')

urlpatterns = router.urls + [
    path('list/', review_list, name='reviews-list'),
]