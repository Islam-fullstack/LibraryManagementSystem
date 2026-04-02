from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=100, verbose_name="Ati")
    description=models.TextField(blank=True, verbose_name="Tusindirmesi")

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name=models.CharField(max_length=255, verbose_name="Ati")
    website=models.URLField(blank=True, verbose_name="Web sayti")
    email=models.EmailField(blank=True, verbose_name="Email")

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=255, verbose_name="Ati")
    bio=models.TextField(blank=True, verbose_name="Tarixi")
    date_of_birth=models.DateField(null=True,blank=True, verbose_name="Tug'ilgan kuni")
    nationality=models.CharField(max_length=100,blank=True, verbose_name="Milleti")

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=255, verbose_name="Atı")
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books', verbose_name="Avtor")
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE,related_name='books', verbose_name="Janrı")
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name='books', verbose_name="Basip shigariwshi")
    isbn=models.CharField(max_length=13,unique=True, verbose_name="ISBN")
    published_date=models.DateField(verbose_name="Basip shigirilgen kuni")
    copies_available=models.PositiveIntegerField(default=0, verbose_name="Bar bolgan nusqalar sani")
    cover_image=models.ImageField(upload_to='book_covers/',blank=True,null=True, verbose_name="Kitap suwreti")

    def __str__(self):
        return self.title
