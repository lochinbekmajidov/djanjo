
from django.contrib import admin
from .models import Category, Book, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "clientname", "address", "clientphone", "category")
    search_fields = ("clientname", "address", "clientphone")
    list_filter = ("category",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "quantity")
    list_filter = ("book",)
