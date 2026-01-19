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

from django.views.generic import TemplateView, ListView, DetailView

class HomeView(TemplateView):
    template_name = 'catalog/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

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
