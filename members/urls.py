from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, RoleViewSet, member_list, member_detail
from . import views

router = DefaultRouter()
router.register(r'', MemberViewSet, basename='member')
router.register(r'', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', member_list, name='members-list'),
    path('<int:pk>/', member_detail, name='member-detail'),
    path('list/', views.member_list, name='members-list'),
]
