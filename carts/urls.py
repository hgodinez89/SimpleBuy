from django.urls import path

# Se importa la vista Cart
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove')
]
