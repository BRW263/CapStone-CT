from django.shortcuts import render
from .models import Item
# Create your views here.
def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", context)

def index(request):
    products =[
        {'title': 'VETMX, 32oz', 'price': 40, 'image': ''},
        {'title': 'Skrim, 20oz', 'price': 30, 'image': ''},
        {'title': 'We All Float, 20oz', 'price': 30, 'image': ''},
        {'title': 'Mama Bear, 16oz', 'price': 20, 'image': ''},
    ]

    context = {
        'products': products,
    }

    return render(request, 'rosies_customs/index.html', context)