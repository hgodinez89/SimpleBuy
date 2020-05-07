from django.contrib import admin
from django.urls import path

from . import views

from django.conf.urls import handler404, handler500

from products.views import ProductListView

from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('language/', views.update_language, name='language'),
    path('', ProductListView.as_view(), name='index'),
    path('users/login', views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
    path('users/register', views.register_view, name='register'),
    path('products/', include('products.urls')),
    path('cart/', include('carts.urls')),
    path('order/', include('orders.urls')),
    path('address/', include('shipping_address.urls')),
    path('codes/', include('promo_codes.urls')),
    path('pays/', include('billing_profiles.urls')),
    path('admin/', admin.site.urls),
]

handler404 = views.handler404
handler500 = views.handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
