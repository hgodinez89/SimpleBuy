# Por convencion se nombra este archivo de esta forma al igual
# que el nombre del folder debe ser templatetags, este folder
# nos permitira implementar nuestros propios filters, los 
# filters son funciones que realizan tareas bastante sencillas

from django import template

from datetime import datetime

# Esto permite registrar funciones como filter
register = template.Library()

# Para hacer el registro se debe decorar la funcion
@register.filter()
def price_format(value):
    return '${0:.2f}'.format(value)

@register.filter()
def date_order_format(value):
    return datetime.strftime(value,'%B %d, %Y')

@register.filter
def total_product_format(value, arg):
    return'${0:.2f}'.format(value * arg)