from django.shortcuts import render
from .models import Product
from .models import Item

# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'rosies_customs/index.html', context)

def item_view(request):
    items = Item.objects.all()

    context = {
        'items': items
    }
    return render(request, 'item_view.html', context)
        


