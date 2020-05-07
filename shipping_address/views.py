from django.shortcuts import render

from django.views.generic import ListView

from .models import ShippingAddress

from .forms import ShippingAddressForm

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import UpdateView, DeleteView

from django.shortcuts import reverse

from django.urls import reverse_lazy

from carts.utils import get_or_create_cart
from orders.utils import get_or_create_order

from django.http import HttpResponseRedirect

from django.utils.translation import gettext_lazy as _

class ShippingAddressListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_address/shipping_address.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')

class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'shipping_address/update.html'
    success_message = _('Address successfully updated')

    def get_success_url(self):
        return reverse('shipping_address:shipping_address')

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')
        
        return super(ShippingAddressUpdateView, self).dispatch(request, *args, **kwargs)

class ShippingAddressDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_address/delete.html'
    success_message = _('Address successfully deleted')
    
    success_url = reverse_lazy('shipping_address:shipping_address')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            messages.error(request, _('The default address cannot be removed.'))
            
            return redirect('shipping_address:shipping_address')
        
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')

        if self.get_object().has_orders():
            messages.error(request, _('The address is associated with an order, therefore it cannot be removed.'))

            return redirect('shipping_address:shipping_address')
        
        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='login')
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not request.user.has_shipping_address()

        shipping_address.save()

        if request.GET.get('next'):
            if request.GET['next'] == reverse('orders:address'):
                cart = get_or_create_cart(request)
                order = get_or_create_order(cart, request)

                order.update_shipping_address(shipping_address)

            messages.success(request, _('Address created successfully'))
            
            return HttpResponseRedirect(request.GET.get('next'))

        messages.success(request, _('Address created successfully'))

        return redirect('shipping_address:shipping_address')

    return render(request, 'shipping_address/create.html', {
        'form': form
    })

@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    if request.user.has_shipping_address():
        request.user.shipping_address.update_default()

    shipping_address.update_default(True)

    messages.success(request, 'Address successfully updated')

    return redirect('shipping_address:shipping_address')