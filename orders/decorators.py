from .utils import get_or_create_order
from carts.utils import get_or_create_cart, add_or_remove_cart_products

def valid_cart_and_order(function):
    def wrap(request, *args, **kwargs):
        cart = get_or_create_cart(request)
        order = get_or_create_order(cart, request)

        add_or_remove_cart_products(request)

        return function(request, cart, order, *args, **kwargs)

    return wrap