from django.urls import path

from . import views

app_name = 'billing_profiles'

urlpatterns = [
    path('new', views.create, name='create'),
    path('default/<int:pk>', views.default, name='default'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('', views.BillingProfileListView.as_view(), name='billing_profiles')
]
