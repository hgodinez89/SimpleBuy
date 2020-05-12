from django.shortcuts import render

from django.conf import settings

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import BillingProfile

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView

from django.http import HttpResponseRedirect

from django.shortcuts import redirect, get_object_or_404

from django.utils.translation import gettext_lazy as _

# Create your views here.
class BillingProfileListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'billing_profiles/billing_profiles.html'

    def get_queryset(self):
        return self.request.user.billing_profiles.order_by('-default')

    def get_context_data(self, **kwargs):
        context = super(BillingProfileListView, self).get_context_data(**kwargs)
        context['billing_profiles'] = self.request.user.billing_profiles.order_by('-default')
        context['choose'] = True if self.request.GET.get('choose') else False

        return context

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        if request.POST.get('stripeToken'):
            if not request.user.has_customer():
                request.user.create_customer_id()
            
            stripe_token = request.POST['stripeToken']
            billing_profile = BillingProfile.objects.create_by_stripe_token(request.user, stripe_token)

            if billing_profile:
                if request.GET.get('next'):
                    messages.success(request, _('Card created successfully. Now you can choose it.'))

                    return HttpResponseRedirect(request.GET.get('next'))
                
                messages.success(request, _('Card created successfully.'))

    return render(request, 'billing_profiles/create.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

@login_required(login_url='login')
def default(request, pk):
    billing_profile = get_object_or_404(BillingProfile, pk=pk)
    
    if request.user.has_billing_profiles():
        billing_profile.update_default(request.user.billing_profile)
    
    billing_profile.update_default(billing_profile, True)

    messages.success(request, _('Card successfully updated.'))

    if request.GET.get('next'):
        return HttpResponseRedirect(request.GET.get('next'))
    
    return redirect('billing_profiles:billing_profiles')

@login_required(login_url='login')
def delete(request, pk):
    billing_profile = get_object_or_404(BillingProfile, pk=pk)
    
    if billing_profile.default:
        messages.error(request, _('The default card cannot be removed.'))
            
        return redirect('billing_profiles:billing_profiles')

    if request.user.id != billing_profile.user_id:
        return redirect('billing_profiles:billing_profiles')

    if billing_profile.has_orders():
        messages.error(request, _('The card is associated with an order, therefore it cannot be removed.'))

        return redirect('billing_profiles:billing_profiles')
       
    BillingProfile.objects.delete_card_stripe(request.user, billing_profile.card_id)

    billing_profile.delete_card()

    messages.success(request, _('Card successfully removed.'))
    
    return redirect('billing_profiles:billing_profiles')