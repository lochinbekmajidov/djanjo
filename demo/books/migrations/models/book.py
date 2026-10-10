from django.db import models

class Book(models.Model):

    clientname= models.CharField("nazvanie", max_length=100)
    address = models.CharField("Adres",max_length=100)
    clientphone = models.IntegerField("Telefon")


class Meta:
        verbose_name = "Kniga"
        verbose_name_plural = "Knigi"

def __str__(self) -> str:
        return self.clientname
    