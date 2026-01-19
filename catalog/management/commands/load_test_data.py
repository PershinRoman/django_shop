"""Кастомная команда для загрузки тестовых данных."""
from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    """Команда load_test_data."""
    help = 'Загружает тестовые данные с удалением старых'

    def handle(self, *args, **kwargs):
        # Удаление старых данных O(n) по моделям
        Product.objects.all().delete()  # Линейно по кол-ву
        Category.objects.all().delete()

        # Загрузка фикстур
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')

        self.stdout.write(self.style.SUCCESS('Данные загружены!'))
