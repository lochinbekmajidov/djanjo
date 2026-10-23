from django.db import models


class Category(models.Model):
    name = models.CharField("Kategoriya nomi", max_length=100)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Book(models.Model):
    clientname = models.CharField("Nomi", max_length=100)
    address = models.CharField("Manzil", max_length=100)
    clientphone = models.CharField("Telefon", max_length=20)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books"
    )

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.clientname


class Order(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    quantity = models.PositiveIntegerField("Miqdori", default=1)

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"

    def __str__(self):
        return self.book.clientname
