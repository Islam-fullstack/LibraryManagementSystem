from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=50, verbose_name="A'za roli")
    description=models.TextField(blank=True, verbose_name="Roli haqida malumat")

    def __str__(self):
        return self.name
    
class Member(models.Model):
    first_name=models.CharField(max_length=255, verbose_name="Atı")
    last_name=models.CharField(max_length=255, verbose_name="Familiyasi")
    email=models.EmailField(unique=True, verbose_name="Email")
    phone_number=models.CharField(max_length=15,blank=True, verbose_name="Telefon nomiri")
    membership_date=models.DateField(auto_now_add=True, verbose_name="A'zaligi baslangan kuni")
    role=models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,blank=True,related_name='members', verbose_name="Roli")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
