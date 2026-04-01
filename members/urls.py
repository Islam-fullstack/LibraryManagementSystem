from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import MemberViewSet, RoleViewSet, member_list, member_detail

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')  # ← named prefix first
router.register(r'', MemberViewSet, basename='member')   # ← '' last

urlpatterns = router.urls + [
    path('list/', member_list, name='members-list'),
    path('<int:pk>/detail/', member_detail, name='member-detail'),
]