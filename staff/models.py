from django.db import models

class Staff(models.Model):
    first_name=models.CharField(max_length=255, verbose_name="Ati")
    last_name=models.CharField(max_length=255, verbose_name="Familiyasi")
    email=models.EmailField(unique=True, verbose_name="Email")
    position=models.CharField(max_length=100, verbose_name="Lawazimi")
    hire_date=models.DateField(auto_now_add=True, verbose_name="Jumisqa kirgen kuni")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

