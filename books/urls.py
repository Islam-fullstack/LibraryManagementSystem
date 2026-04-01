from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, GenreViewSet, PublisherViewSet
from . import views

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('genres', GenreViewSet)
router.register('publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
