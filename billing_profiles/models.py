from django.db import models

from users.models import User

from stripeAPI.card import create_card, remove_card

# Create your models here.
class BillingProfileManager(models.Manager):

    def create_by_stripe_token(self, user, stripe_token):
        if user.has_customer() and stripe_token:
            source = create_card(user, stripe_token)

            return self.create(card_id=source.id,
                               last4=source.last4,
                               token=stripe_token,
                               brand=source.brand,
                               exp_month=source.exp_month,
                               exp_year=source.exp_year,
                               user=user,
                               default=not user.has_billing_profiles())

    def delete_card_stripe(self, user, card_id):
        if user.has_customer():
            response = remove_card(card_id, user)
        
class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=False, blank=False)
    card_id = models.CharField(max_length=50, null=False, blank=False)
    last4 = models.CharField(max_length=4, null=False, blank=False)
    brand = models.CharField(max_length=10, null=False, blank=False)
    exp_month = models.IntegerField(null=False, blank=False)
    exp_year = models.IntegerField(null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BillingProfileManager()

    def __str__(self):
        return self.card_id

    def update_default(self, billing_profile, default=False):
        billing_profile.default = default
        billing_profile.save()
    
    def delete_card(self):
        self.delete()
    
    def has_orders(self):
        return self.order_set.count() >= 1