from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

from .utils import get_or_create_cart, add_or_remove_cart_products

from products.models import Product

from .models import CartProducts

# Create your views here.
def cart(request):
    cart = get_or_create_cart(request)
    add_or_remove_cart_products(request)

    return render(request, 'carts/cart.html', {
        'cart': cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)

    add_or_remove_cart_products(request)

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'cart_product' :  cart_product,
        'product': product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    add_or_remove_cart_products(request)
    
    return redirect('carts:cart')