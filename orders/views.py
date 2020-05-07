from django.shortcuts import render

from carts.utils import destroy_cart

from .utils import get_or_create_order, breadcrumb, destroy_order

from .models import Order

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from django.shortcuts import redirect

from shipping_address.models import ShippingAddress

from django.contrib import messages

from .mails import Mail

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from django.db.models.query import EmptyQuerySet

from .decorators import valid_cart_and_order

from charges.models import Charge

from django.db import transaction

from django.utils.translation import gettext_lazy as _

import threading

# Create your views here.
class OrderListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return self.request.user.orders_completed()

@login_required(login_url='login')
@valid_cart_and_order
def order(request, cart, order):
    if not cart.has_products():
        return redirect('carts:cart')

    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })

@login_required(login_url='login')
@valid_cart_and_order
def address(request, cart, order):
    if not cart.has_products():
        return redirect('carts:cart')

    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.has_shipping_addresses

    return render(request, 'orders/address.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb': breadcrumb(address=True, currentStep='shipping'),
        'can_choose_address': can_choose_address
    })

@login_required(login_url='login')
@valid_cart_and_order
def select_address(request, cart, order):
    shipping_address = request.user.addresses
    shipping_address_order = order.get_or_set_shipping_address()

    return render(request, 'orders/select_address.html', {
        'breadcrumb': breadcrumb(address=True, currentStep='shipping'),
        'address_used': shipping_address_order.pk,
        'shipping_address': shipping_address
    })

@login_required(login_url='login')
@valid_cart_and_order
def check_address(request, cart, order, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')
    
    order.update_shipping_address(shipping_address)

    return redirect('orders:address')

@login_required(login_url='login')
@valid_cart_and_order
def confirm(request, cart, order):
    if not cart.has_products() or order.shipping_address is None or order.billing_profile is None:
        return redirect('carts:cart')

    shipping_address = order.shipping_address

    if shipping_address is None:
        redirect('orders:address')
    
    return render(request, 'orders/confirm.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb': breadcrumb(address=True, payment=True, confirmation=True, currentStep='confirm')
    })

@login_required(login_url='login')
@valid_cart_and_order
def cancel(request, cart, order):
    if request.user.id != order.user_id:
        return redirect('carts:cart')

    order.cancel()

    destroy_cart(request)
    destroy_order(request)

    messages.error(request, _('Order cancelled'))

    return redirect('index')

@login_required(login_url='login')
@valid_cart_and_order
def complete(request, cart, order):
    if request.user.id != order.user_id:
        return redirect('carts:cart')

    charge = Charge.objects.create_charge(order)

    if charge:
        with transaction.atomic():
            order.complete()

            thread = threading.Thread(target=Mail.send_complete_order, args=(
                order, request.user
            ))

            thread.start()

            destroy_cart(request)
            destroy_order(request)

            messages.success(request, _('Purchase successfully completed'))

    return redirect('index')

@login_required(login_url='login')
@valid_cart_and_order
def payment(request, cart, order):
    if not cart.has_products() or order.shipping_address is None:
        return redirect('carts:cart')

    billing_profile = order.get_or_set_billing_profile()

    return render(request, 'orders/payment.html', {
        'cart': cart,
        'order': order,
        'billing_profile': billing_profile,
        'breadcrumb': breadcrumb(address=True, payment=True, currentStep='payment')
    })