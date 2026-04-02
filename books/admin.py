from django.contrib import admin
from .models import Author,Book,Genre,Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','date_of_birth','nationality')
    search_fields=('name','nationality')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'published_date', 'copies_available')
    list_filter = ('published_date', 'genre', 'publisher')
    search_fields = ('title', 'isbn')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')
    search_fields = ('name',)

admin.site.site_header = "Kitapxana Basqarıw Sisteması"
admin.site.site_title = "Kitapxana Admin Paneli"
admin.site.index_title = "Sistemani Basqarıw"