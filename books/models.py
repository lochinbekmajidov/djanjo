
from django.db import models


class Kategoriya(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.nomi


class Book(models.Model):
    clientname = models.CharField("Nazvanie", max_length=100)
    address = models.CharField("Adres", max_length=100)
    clientphone = models.IntegerField("Telefon")

    class Meta:
        verbose_name = "Kniga"
        verbose_name_plural = "Knigi"

    def __str__(self):
        return self.clientname


class Knigi(models.Model):
    nomi = models.CharField(max_length=200)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    kategoriya = models.ForeignKey(
        Kategoriya,
        on_delete=models.CASCADE,
        related_name="kitoblar"
    )
    tavsifi = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.nomi
