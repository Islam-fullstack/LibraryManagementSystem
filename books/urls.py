from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, GenreViewSet, PublisherViewSet
from . import views

router = DefaultRouter()
router.register('', AuthorViewSet)
router.register('', BookViewSet)
router.register('', GenreViewSet)
router.register('', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
