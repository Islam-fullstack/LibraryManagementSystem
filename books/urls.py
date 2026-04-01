from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, GenreViewSet, PublisherViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'publishers', PublisherViewSet, basename='publisher')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'', BookViewSet, basename='book')  # ← '' must be LAST

urlpatterns = router.urls