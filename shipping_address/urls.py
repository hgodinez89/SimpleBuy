from django.urls import path

from . import views

app_name = 'shipping_address'

urlpatterns = [
    path('', views.ShippingAddressListView.as_view(), name='shipping_address'),
    path('new', views.create, name='create'),
    path('edit/<int:pk>', views.ShippingAddressUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ShippingAddressDeleteView.as_view(), name='delete'),
    path('default/<int:pk>', views.default, name='default')
]