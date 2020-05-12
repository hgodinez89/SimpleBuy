from django.forms import ModelForm

from .models import ShippingAddress

from django.utils.translation import gettext_lazy as _

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'postal_code',
            'reference'
        ]
        labels = {
            'line1': _('Address 1'),
            'line2': _('Address 2'),
            'city': _('City'),
            'state': _('State/Province'),
            'country': _('Country'),
            'postal_code': _('Zip Code'),
            'reference': _('Other')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['line1'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10',
            'placeholder': _('Street address, P.O. box, company name, etc')
        })
        self.fields['line2'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10',
            'placeholder': _('Apartment, suite, unit, building, floor, etc')
        })
        self.fields['city'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10'
        })
        self.fields['state'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10'
        })
        self.fields['country'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10'
        })
        self.fields['postal_code'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10'
        })
        self.fields['reference'].widget.attrs.update({
            'class': 'text-sm appearance-none rounded w-full py-2 px-3 text-gray-700 bg-gray-200 leading-tight focus:outline-none focus:shadow-outline h-10',
            'placeholder': _('Details such as building description, a nearby landmark, etc')
        })
    
