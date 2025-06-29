from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Fill database with test products"

    def handle(self, *args, **options):
        # Удаляем все продукты и категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        electronics = Category.objects.create(name="Электроника", description="Гаджеты")
        clothing = Category.objects.create(name="Одежда", description="Модная одежда")

        # Создаем продукты
        products = [
            {
                "name": "Смартфон",
                "description": "Новый смартфон",
                "category": electronics,
                "price": 50000,
            },
            {
                "name": "Ноутбук",
                "description": "Мощный ноутбук",
                "category": electronics,
                "price": 80000,
            },
            {
                "name": "Футболка",
                "description": "Хлопковая футболка",
                "category": clothing,
                "price": 1500,
            },
        ]

        for product in products:
            Product.objects.create(**product)

        self.stdout.write(self.style.SUCCESS("Successfully filled products"))
