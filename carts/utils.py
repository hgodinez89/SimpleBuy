from .models import Cart


def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart

def add_or_remove_cart_products(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()

    productsQuantity = 0 
    
    if cart is not None:
        for product in cart.cartproducts_set.select_related('product'):
            productsQuantity += product.quantity
             
    request.session['products_quantity'] = productsQuantity

def destroy_cart(request):
    request.session['cart_id'] = None
    request.session['products_quantity'] = 0
