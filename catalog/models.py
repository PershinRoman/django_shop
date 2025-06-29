from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Изображение",
        null=True,
        blank=True,
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Дата создания"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_al = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'