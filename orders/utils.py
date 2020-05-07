from .models import Order

from django.urls import reverse

from django.utils.translation import gettext_lazy as _

breadcrumb_steps = ['products', 'shipping', 'payment', 'confirm']


def get_or_create_order(cart, request):
    order = cart.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)

    if order:
        request.session['order_id'] = order.order_id

    return order


def breadcrumb(products=True, address=False, payment=False, confirmation=False, currentStep='products'):
    return [
        {'title': _('Products'), 'active': products, 'url': reverse(
            'orders:order'), 'state': state_step_breadcrumb(currentStep, 'products'), 'step': '1'},
        {'title': _('Shipping'), 'active': address,
         'url': reverse('orders:address'), 'state': state_step_breadcrumb(currentStep, 'shipping'), 'step': '2'},
        {'title': _('Payment'), 'active': payment,
         'url': reverse('orders:payment'), 'state': state_step_breadcrumb(currentStep, 'payment'), 'step': '3'},
        {'title': _('Place order'), 'active': confirmation,
         'url': reverse('orders:confirm'), 'state': state_step_breadcrumb(currentStep, 'confirm'), 'step': '4'}
    ]


def state_step_breadcrumb(currentStep, stepName):
    if stepName in breadcrumb_steps and currentStep in breadcrumb_steps:
        indexStepName = breadcrumb_steps.index(stepName)
        indexCurrentStep = breadcrumb_steps.index(currentStep)

        if indexStepName == indexCurrentStep:
            return 'progress'
        elif indexStepName < indexCurrentStep:
            return 'completed'
        else:
            return 'pending'


def destroy_order(request):
    request.session['order_id'] = None
