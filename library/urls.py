from django.contrib import admin
from django.urls import path,include
from books.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),          # ← home only, no duplicate path('')
    path('api/books/', include('books.urls')),
    path('api/members/', include('members.urls')),
    path('api/borrowing/', include('borrowing.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/reviews/', include('reviews.urls')),
]