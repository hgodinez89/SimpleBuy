from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib.auth import authenticate

from django.contrib.auth import login

from django.contrib.auth import logout

from django.contrib import messages

from .forms import RegisterForm

from users.models import User

from products.models import Product

from django.http import HttpResponseRedirect

from django.utils import translation

from django.views.i18n import set_language

from django.utils.translation import gettext_lazy as _

def index(request):
    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'message': _('Product List'),
        'title': _('Products'),
        'products': products
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            translation.activate(request.user.language)
            
            messages.success(request, _('Welcome') + ' {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
        else:
            messages.error(request, _('Invalid user or password'))

    return render(request, 'users/login.html', {

    })


def logout_view(request):
    logout(request)
    messages.success(request, _('Session ended successfully'))

    translation.deactivate()

    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, _('User successfully created'))
            
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })

def update_language(request):
    if request.user.is_authenticated and request.method == 'POST':
        request.user.language = request.POST.get('language')

        request.user.save()

    translation.activate(request.POST.get('language'))

    return set_language(request)

def handler404(request, *args):
    return render(request, '404.html', status=404)

def handler500(request, *args):
    return render(request, '500.html', status=500)
