from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django import forms
from django.core.paginator import Paginator  # Для пагинации
from .models import Product, Category, Contact
# Форма контактов (как раньше)

class ContactForm(forms.Form):
    """Форма для обратной связи."""
    # ... (как раньше)

# Доп: Форма для продукта
class ProductForm(forms.ModelForm):
    """Форма для создания продукта."""
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean(self):
        """Валидация: проверка типов и очистка."""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name and not isinstance(name, str):
            raise forms.ValidationError("Наименование должно быть строкой.")
        if name:
            cleaned_data['name'] = name.strip()  # Очистка пробелов
        return cleaned_data

def home(request):
    """Контроллер для домашней страницы."""
    # Все продукты O(n), но пагинация ограничивает
    products_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products_list, 5)  # 5 на страницу, линейная память
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Доп: последние 5 в консоль (как раньше)
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Product: {product.name}, Price: {product.price}")
    return render(request, 'catalog/home.html', {'page_obj': page_obj})

def contacts(request):
    """Контроллер для страницы контактов с формой."""
    # ... (как раньше, с contacts_data)

def product_detail(request, pk):
    """Контроллер для страницы товара."""
    # Получаем продукт O(1)
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def product_create(request):
    """Контроллер для создания продукта (доп)."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # FILES для image
        if form.is_valid():
            form.save()  # Сохраняет в БД
            return redirect('home')  # Перенаправление
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})
