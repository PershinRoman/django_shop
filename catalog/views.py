from django.shortcuts import render
from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f"{product.name} - {product.price}")

    return render(request, 'home.html')

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})
