from django.shortcuts import render

# Create your views here.
def index(request):
    products = [
        {'title': 'VetMX', 'price': 35, 'image': '' },
        {'title': 'Skyrim', 'price': 25, 'image': ''},
        {'title': 'We All Float', 'price': 25, 'image': ''},

    ]

    context = {
        'products': products,
    }
    return render(request, 'webapp/index.html', context)