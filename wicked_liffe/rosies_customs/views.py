from django.shortcuts import render
from .models import Item
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

def logout_view(request):
    logout(request)
    

@login_required
def my_view(request):
    return render(request,"item_list")


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", context)

def index(request):
    products = Item.object.all()

    context = {
        'products': products,
    }

    return render(request, 'rosies_customs/index.html', context)