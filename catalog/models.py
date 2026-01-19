"""Модели приложения catalog."""
from django.db import models

class Category(models.Model):
    """Модель категории продуктов."""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def clean(self):
        """Валидация: проверка типов и очистка."""
        if not isinstance(self.name, str):
            raise ValueError("Наименование должно быть строкой.")
        self.name = self.name.strip()  # Очистка пробелов

class Product(models.Model):
    """Модель продукта."""
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', null=True, blank=True,
                              verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def clean(self):
        """Валидация: проверка типов и очистка."""
        if not isinstance(self.name, str):
            raise ValueError("Наименование должно быть строкой.")
        if not isinstance(self.price, (int, float)):
            raise ValueError("Цена должна быть числом.")
        self.name = self.name.strip()  # Очистка пробелов, акценты в Unicode OK

class Contact(models.Model):
    """Модель контактных данных."""
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name