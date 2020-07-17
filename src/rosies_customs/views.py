from django.shortcuts import render, redirect
from .models import Product, ProductImage



# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'rosies_customs/index.html', context)

def single(request, slug):
    product = Product.objects.get(slug=slug)
    products = Product.objects.all()
    context = {
        'products': products
    }
    template = 'products/single.html'
    return render(request, 'rosies_customs/index.html', context)