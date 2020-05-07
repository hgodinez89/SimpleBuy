from django import template

from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.filter()
def quantity_product_format(quantity=1):
    return '{} {}'.format(quantity, _('products') if quantity > 1 else _('product'))


@register.filter()
def quantity_add_format(quantity=1):
    return '{} {}'.format(
        quantity_product_format(quantity),
        _('added ') if quantity > 1 else _('added')
    )


@register.filter()
def empty_cart_format(quantity):
    return 0 if quantity == "" else quantity


@register.filter()
def subtotal_quantity_format(quantity=1):
    return '{} {}'.format(
        quantity,
        _('items') if quantity > 1 else _('item')
    )
