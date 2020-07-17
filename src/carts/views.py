from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.core.urlresolvers import reverse
from .models import Cart
from rosies_customs.models import Product



# Create your views here.
def view(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "cart/view.html"
    return render(request, template, context)


def update_cart(request,):
    cart = Cart.objects.all()
    try:
        product = Product.objects.get()
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    return HttpResponseRedirect('cart')
    new_total = 0.00
    for item in cart.products.all():
        new_total += float (item.price)
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))


