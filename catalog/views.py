from django.shortcuts import render
from catalog.models import Product


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f"{product.name} - {product.price}")

    return render(request, 'home.html')
