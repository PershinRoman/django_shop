from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Product, Contact  # Для доп. задания

# ... (ContactForm как раньше)

def home(request):
    """Контроллер для домашней страницы."""
    # Доп. задание: последние 5 продуктов, O(n) с limit
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Product: {product.name}, Price: {product.price}")  # В консоль
    return render(request, 'catalog/home.html')

def contacts(request):
    """Контроллер для страницы контактов с формой."""
    # Доп. задание: контакты из БД
    contacts_data = Contact.objects.all()  # O(n) линейно
    context = {'form': ContactForm(), 'contacts': contacts_data}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Сообщение отправлено успешно!')
        else:
            context['form'] = form
    return render(request, 'catalog/contacts.html', context)
